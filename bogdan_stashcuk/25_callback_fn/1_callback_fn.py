def fn():
    print("empty fn")


def fn_with_callback(other_fn):
    other_fn()


fn_var = fn
fn_with_callback(fn_var)


def print_number_info(num):
    print(f"Выполняется обработка числа {num} в 1-й функции")


def print_number_add_info(num):
    print(f"Выполняется обработка числа {num} в 2-й функции")


def process_number(num, *fns):
    for f in fns:
        f(num)


process_number(10, print_number_info, print_number_add_info)
process_number(10, print)
