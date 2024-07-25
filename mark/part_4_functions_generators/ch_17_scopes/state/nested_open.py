# Рекурсивно вложенное состояние с памятью
from helpers import print_section


def program_1():
    print_section("program_1(): Рекурсивно вложенное состояние с памятью")

    class Action:

        def __init__(self):
            pass

        def make_example(self, text='default'):
            print(f'text={text}')

    instance = Action()

    # instance.make_example('hi')

    def change_example(message):
        original = instance.make_example

        def custom(text):
            print(f'{message}={text}')
            original(text)

        instance.make_example = custom

    change_example('new text')
    instance.make_example('hi')
    change_example('again new text')
    instance.make_example('hi')


# Рекурсивно вложенное состояние с памятью
program_1()
