"""
Print decision algorithm combination for documentation
"""

from abac.policy_administration_point.const import DENY, PERMIT, NOT_APPLICABLE, INDETERMINATE

DECISIONS = [PERMIT, DENY, NOT_APPLICABLE, INDETERMINATE]
BOLD = '**'
NORMAL = '</span>'
RED = '<span style="color:red">'
GREEN = '<span style="color:green">'
BLUE = '<span style="color:blue">'
WHITE = '<span>'

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

str_row = '|' + '{:^{length}} |'*(COUNT_COLUMN+1)
str_color_row = '|' + '{:^{length}} |' + '{:^{color_length}} |'*COUNT_COLUMN
str_line = '|' + ('-'*(LENGTH + 1) + '|')*(COUNT_COLUMN + 1)


def print_decision_combination(alg):
    print('### ' + alg.__name__.upper())
    print()
    print(str_row.format('', *DECISIONS, length=LENGTH))
    print(str_line)
    for decision in DECISIONS:
        print(str_color_row.format(
            '**{}**'.format(decision),
            *[COLOR_DECISIONS[alg([decision, d])] for d in DECISIONS],
            length=LENGTH,
            color_length=COLOR_LENGTH
        ))
    print()

