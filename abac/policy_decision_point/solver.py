import collections

from django.contrib.auth.base_user import AbstractBaseUser

from abac.policy_administration_point import Policy, PolicySet


class Solver:

    def __init__(self, user, resource, action, policies):
        self.user = user
        self.resource = resource
        self.action = action
        self.policies = policies
        self.validate_initialization()

    def validate_initialization(self):
        if not isinstance(self.user, AbstractBaseUser):
            raise TypeError('The user must be an instance of django.contrib.auth.models.AbstractBaseUser cls')
        if not isinstance(self.policies, collections.Iterable):
            raise TypeError('The policies is not iterable')
        for policy in self.policies:
            if not isinstance(policy, (Policy, PolicySet)):
                raise TypeError('The policy is not Policy or PolicySet')

    def decision(self):
        if isinstance(self.target, bool):
            target = self.target
        else:
            target = self.target.decision()
        try:
            if target is True:
                return self.algorithm(
                    [rule.decision() for rule in self.rules]
                )
            return NOT_APPLICABLE
        except Exception as e:
            self.error = e
            return INDETERMINATE