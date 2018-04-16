import abac.policy_administration_point.expressions as expressions
import inspect
from abac import decorators

columns = (20, 20, 20)
row = '{:%d}|{:%d}|{:%d}' % columns


def print_classes():
    print(decorators.expression.__doc__)
    # print(row.format(
    #     'Наименование выражения',
    #     'Обязательные параметры',
    #     'Описание',
    # ))
    # print(row.format(*['-'*column for column in columns]))
    # for name, obj in inspect.getmembers(expressions, inspect.isclass):
    #     sig = inspect.signature(obj)
    #     print(row.format(
    #         name,
    #         ', '.join(sig.parameters.keys()),
    #     ))


print_classes()