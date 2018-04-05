from django.contrib.auth.base_user import AbstractBaseUser
from django.core.cache import cache

from abac.settings import abac_settings


class AbstractCondition:

    def condition(self) -> bool:
        """ A set of condition for calculating rule """
        raise NotImplementedError('Subclasses must implement this method.')


class UserGroupIsCondition(AbstractCondition):

    def __init__(self, user, group_name):
        self.user = user
        self.group_name = group_name
        self.validate_initialization()

    def condition(self):
        condition = cache.get_or_set(
            'abac.user_group_is.{}.{}'.format(self.user.id, self.group_name),
            self.user.groups.filter(name=self.group_name).exists(),
            abac_settings.CACHE_RULE_TIMEOUT
        )
        return bool(condition)

    def validate_initialization(self):
        if not isinstance(self.user, AbstractBaseUser):
            raise TypeError('The user must be an instance of django.contrib.auth.models.AbstractBaseUser cls.')
        if not isinstance(self.group_name, str):
            raise TypeError('The my_group must be a str')


class EqualCondition(AbstractCondition):

    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.validate_initialization()

    def condition(self):
        return self.first == self.second

    def validate_initialization(self):
        if not isinstance(self.first, type(self.second)):
            raise TypeError('The first and second parameterss must be of the same type')
