from django.contrib.auth.models import AbstractBaseUser
from django.core.cache import cache

from abac.policy_administration_point.const import NOT_APPLICABLE, INDETERMINATE, PERMIT
from abac.settings import settings

class AbstractRule:
    """ Abstract class describing the basic behavior of the entity "rule" """

    def decision(self):
        try:
            if self.target():
                if self.condition():
                    return self.effect
            return NOT_APPLICABLE
        except Exception:
            return INDETERMINATE

    def target(self):
        """ Returns the result of calculating the target """
        raise NotImplementedError('Subclasses must implement this method.')

    def condition(self):
        """ Returns the result of calculating the condition """
        raise NotImplementedError('Subclasses must implement this method.')

    @property
    def effect(self):
        """ Return effect condition """
        return PERMIT

    def obligation(self):
        """ Function that fulfills the obligations imposed on the rules """
        pass

    def advice(self):
        """ Function that fulfills the advices imposed on the rules """
        pass

    def description(self):
        """ Return text description the rule """
        pass

    def __str__(self):
        return type(self).__name__


class UserGroupIsRule(AbstractRule):
    """ Verify that the user belongs to the specified role """
    def __init__(self, user, group_name):
        if not isinstance(user, AbstractBaseUser):
            raise TypeError('The user must be an instance of django.contrib.auth.models.AbstractBaseUser cls.')
        self.user = user
        self.group_name = group_name

    def target(self):
        return True

    def condition(self):
        condition = cache.get_or_set(
            'abac.user_group_is.{}.{}'.format(self.user.id, self.group_name),
            self.user.groups.filter(name=self.group_name).exists(),
            settings.CACHE_RULE_TIMEOUT
        )
        return bool(condition)


class ActionIsRule(AbstractRule):
    """ Verify that the action is specified """
    def __init__(self, action, need_action):
        self.action = action
        self.need_action = need_action

    def target(self):
        return True

    def condition(self):
        return self.action == self.need_action