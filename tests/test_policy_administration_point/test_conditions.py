import pytest

from django.contrib.auth.models import User, Group
from django.test import TestCase

from abac.policy_administration_point import (
    EqualExpressions, UserGroupIsExpressions
)


class ConditionTests(TestCase):
    """ Test the PAP decision """

    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret'
        )
        # Create correct group
        self.correct_group_name = 'new_group'
        self.correct_group = Group.objects.create(name=self.correct_group_name)
        self.user.groups.add(self.correct_group)
        # Create bad group
        self.bad_group_name = 'bad_group'
        Group.objects.create(name=self.bad_group_name)

    def test_equal_condition_true(self):
        condition = EqualExpressions('test', 'test')
        self.assertEqual(condition.decision(), True)

    def test_equal_condition_false(self):
        condition = EqualExpressions('first', 'second')
        self.assertEqual(condition.decision(), False)

    def test_equal_condition_exception(self):
        with pytest.raises(TypeError):
            EqualExpressions('test', 123)

    def test_user_is_group_condition_true(self):
        condition = UserGroupIsExpressions(
            self.user, self.correct_group_name
        )
        self.assertEqual(condition.decision(), True)

    def test_user_is_group_condition_false(self):
        condition = UserGroupIsExpressions(
            self.user, self.bad_group_name
        )
        self.assertEqual(condition.decision(), False)

    def test_user_is_group_condition_exception(self):
        with pytest.raises(TypeError):
            UserGroupIsExpressions(
                self.user, self.correct_group
            )

