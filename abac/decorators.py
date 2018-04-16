import inspect


def print_expression(name, params, description):
    columns = (20, 20, 20)
    row = '{:%d}|{:%d}|{:%d}' % columns
    print(row.format(name, params, description))


def expression(func):
    """ Registration expression decorator """
    name = func.__name__
    params = ', '.join(inspect.signature(func).parameters.keys())
    description = func.__doc__
    print_expression(name, params, description)
    return func
