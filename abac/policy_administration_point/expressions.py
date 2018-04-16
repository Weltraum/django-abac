from django.core.cache import cache

from abac.settings import abac_settings
from abac.decorators import expression


@expression
def user_group_is(user, group):
    """ Defines the group membership """
    decision = cache.get_or_set(
        'abac.user_group_is.{}.{}'.format(user.id, group),
        user.groups.filter(name=group).exists(),
        abac_settings.CACHE_RULE_TIMEOUT
    )
    return bool(decision)


@expression
def equal(first, second):
    """ Comparison of two values """
    return first == second
