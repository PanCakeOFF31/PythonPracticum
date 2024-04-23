def block_hello():
    print('Hello from function body')


def inline_hello(): print('Hello from inline function')


def fn_with_arg(arg):
    print('Вызов функции с аргументом:', arg)


block_hello()
inline_hello()

# Присваивание функции другой переменной
hello = block_hello
hello()

# Присваивание функции другой переменной
hello = inline_hello
hello()

fn_with_arg('The greatest argument')
# Вызов функции ниже приведет к ошибке: отсутствует обязательный аргумент
# fn_with_arg()
