from django.contrib.auth.models import User, Group
from django.test import TestCase

from abac.policy_administration_point import Rule
from abac.policy_administration_point.expressions import user_group_is
from abac.const import PERMIT, DENY, NOT_APPLICABLE


class RulesTests(TestCase):
    """ Test the PAP rules """

    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret'
        )
        self.my_group_name = 'new_group'
        self.my_group = Group.objects.create(name=self.my_group_name)
        self.user.groups.add(self.my_group)

    def test_create_rule_permit(self):
        user_is_my_group_rule = Rule(
            condition=user_group_is,
            condition_param=dict(
                user=self.user, group=self.my_group_name
            ),
            effect=PERMIT,
        )
        self.assertEqual(
            user_is_my_group_rule.decision(),
            PERMIT,
            user_is_my_group_rule.error
        )

    def test_create_rule_deny(self):
        user_is_my_group_rule = Rule(
            condition=user_group_is,
            condition_param=dict(
                user=self.user, group=self.my_group_name
            ),
            effect=DENY,
        )
        self.assertEqual(
            user_is_my_group_rule.decision(),
            DENY,
            user_is_my_group_rule.error
        )

    def test_create_rule_not_applicable(self):
        user_is_my_group_rule = Rule(
            condition=user_group_is,
            condition_param=dict(
                user=self.user, group='test'
            ),
        )
        self.assertEqual(
            user_is_my_group_rule.decision(),
            NOT_APPLICABLE,
            user_is_my_group_rule.error
        )
