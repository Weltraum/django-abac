from django.contrib.auth.models import User, Group
from django.test import TestCase

from abac.policy_administration_point import PolicySet, Policy, Rule
from abac.policy_administration_point.expressions import user_group_is, equal
from abac.algorithm import permit_overrides
from abac.const import PERMIT


class PolicySetTests(TestCase):
    """ Test the PAP policy set """

    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret'
        )
        self.my_group_name = 'new_group'
        self.my_group = Group.objects.create(name=self.my_group_name)
        self.user.groups.add(self.my_group)
        self.user_is_my_group_rule = Rule(
            condition=user_group_is,
            condition_param=dict(
                user=self.user, group=self.my_group_name
            ),
            effect=PERMIT,
        )
        self.policy = Policy(
            target=equal,
            target_param=dict(first='test', second='test'),
            rules=[self.user_is_my_group_rule],
            algorithm=permit_overrides
        )

    def test_create_policy(self):
        policy_set = PolicySet(
            target=equal,
            target_param=dict(first='test', second='test'),
            policies=[self.policy],
            algorithm=permit_overrides
        )
        self.assertEqual(
            policy_set.decision(),
            PERMIT,
            policy_set.error
        )
