import abac.policy_administration_point.expressions as expressions
import inspect

columns = (23, 23, 35)
row = '{:%d}|{:%d}|{:%d}' % columns


def print_classes():
    print(row.format(
        'Наименование класса',
        'Обязательные параметры',
        'Принадлежность AbstractExpressions',
    ))
    print(row.format(*['-'*column for column in columns]))
    for name, obj in inspect.getmembers(expressions, inspect.isclass):
        if inspect.getmro(obj)[0] == expressions.AbstractExpressions: continue
        sig = inspect.signature(obj)
        print(row.format(
            name,
            ', '.join(sig.parameters.keys()),
            expressions.AbstractExpressions in inspect.getmro(obj)
        ))


print_classes()