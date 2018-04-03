from abac.policy_administration_point.const import DENY, PERMIT, NOT_APPLICABLE, INDETERMINATE

DECISIONS = [PERMIT, DENY, NOT_APPLICABLE, INDETERMINATE]

BOLD = '\x1b[1m'
NORMAL = '\x1b[0m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
BLUE = '\x1b[34m'
WHITE = '\x1b[30m'

str_color = '{color}{decision}{normal}'

COLOR_DECISIONS = {
    PERMIT: str_color.format(
        color=GREEN,
        decision=PERMIT,
        normal=NORMAL,
    ),
    DENY: str_color.format(
        color=RED,
        decision=DENY,
        normal=NORMAL,
    ),
    NOT_APPLICABLE: str_color.format(
        color=WHITE,
        decision=NOT_APPLICABLE,
        normal=NORMAL,
    ),
    INDETERMINATE: str_color.format(
        color=BLUE,
        decision=INDETERMINATE,
        normal=NORMAL,
    ),
}

LENGTH = 21
COLOR_LENGTH = 30
COUNT_COLUMN = len(DECISIONS)

str_row = '{:^{length}} |'*(COUNT_COLUMN+1)
str_color_row = '{:^{length}} |' + '{:^{color_length}} |'*COUNT_COLUMN
str_line = '-'*(COUNT_COLUMN + 1)*(LENGTH + 2)


def print_decision_combination(alg):
    print(str_color.format(
        color=BOLD,
        decision=alg.__name__.upper(),
        normal=NORMAL
    ))
    print(str_line)
    print(str_row.format('', *DECISIONS, length=LENGTH))
    print(str_line)
    for decision in DECISIONS:
        print(str_color_row.format(
            decision,
            *[COLOR_DECISIONS[alg([decision, d])] for d in DECISIONS],
            length=LENGTH,
            color_length=COLOR_LENGTH
        ))
        print(str_row.format(*['']*5, length=LENGTH))
    print()

