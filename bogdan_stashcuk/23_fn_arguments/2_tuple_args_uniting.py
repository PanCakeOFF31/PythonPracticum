def sum_args_1(*args):
    print('values:', args)


def sum_args_2(a, *values):
    print('a:', a)
    print('values:', values)


def sum_args_3(*values, a):
    print('a:', a)
    print('values:', values)


def sum_args_4(*values):
    print('values:', values, type(values))


sum_args_1(10, '👌', 30)
sum_args_2(10, '👌', 30)
# keyword-only
sum_args_3(10, '👌', a=30)
sum_args_4(10, '👌', '😍')
