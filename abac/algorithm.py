"""
http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html#_Toc325047268
"""

from abac.const import (
    PERMIT, DENY, INDETERMINATE, NOT_APPLICABLE
)


def deny_overrides(decisions):
    one_permit = False
    one_indeterminate = False
    for decision in decisions:
        if decision == DENY:
            return DENY
        if decision == PERMIT:
            one_permit = True
            continue
        if decision == NOT_APPLICABLE:
            continue
        if decision == INDETERMINATE:
            one_indeterminate = True
            continue
    if one_indeterminate:
        return INDETERMINATE
    if one_permit:
        return PERMIT
    return NOT_APPLICABLE


def permit_overrides(decisions):
    one_deny = False
    one_indeterminate = False
    for decision in decisions:
        if decision == DENY:
            one_deny = True
            continue
        if decision == PERMIT:
            return PERMIT
        if decision == NOT_APPLICABLE:
            continue
        if decision == INDETERMINATE:
            one_indeterminate = True
            continue
    if one_indeterminate:
        return INDETERMINATE
    if one_deny:
        return DENY
    return NOT_APPLICABLE


def deny_unless_permit(decisions):
    if PERMIT in decisions:
        return PERMIT
    return DENY


def permit_unless_deny(decisions):
    if DENY in decisions:
        return DENY
    return PERMIT
