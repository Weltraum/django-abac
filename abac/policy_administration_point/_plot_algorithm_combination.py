from abac.policy_administration_point.plot_algorithm_combination import print_decision_combination
from abac.algorithm import (
    permit_unless_deny,
    deny_unless_permit,
    permit_overrides,
    deny_overrides
)

ALGS = [
    permit_unless_deny,
    deny_unless_permit,
    permit_overrides,
    deny_overrides
]

for alg in ALGS:
    print_decision_combination(alg)