from helpers import print_section


def program_1(index: int):
    collection = [10, 20]
    try:
        print(collection[index])
    except Exception as a:
        print("Было исключение")
    else:
        print("Не было исключения")
    finally:
        print("В любом случае")


print_section('try except else finally')
program_1(0)


def program_2():
    for i in range(4):
        break
    else:
        print("Не прошли до конца")


print_section('Хрень с for else')
program_2()


# list comprehension
# list comprehension expression
def program_3():
    collect = [15, 15.0, 33, 1, 3, 9]
    print(collect)

    mapped = [['Исходное число:',
               number,
               'это же число в квадрате',
               number ** 2]
              for number in collect
              if 20 >= number > 0]

    print(type(mapped))
    print(type(mapped[0]))
    for record in mapped:
        print(record)


# list comprehension as generator
def program_4():
    collect = [15, 15.0, 33, 1, 3, 9]
    print(collect)

    mapped = (['Исходное число:',
               number,
               'это же число в квадрате',
               number ** 2]
              for number in collect
              if 20 >= number > 0)

    print(type(mapped))
    print(type(next(mapped)))
    for record in mapped:
        print(record)


print_section("List comprehension")
program_3()
program_4()


# generator from comprehension
def program_5():
    generator = (i for i in range(3))
    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())


print_section('Generator from range comprehension')
program_5()


def program_6():
    def process(a: int, b: int) -> int:
        return (a + b) * 2

    collection = [10, 20, 30]
    print(collection)
    print(list(map(process, *collection)))
    return


print_section("Не понятно мне как это работает аааа...")
# program_6()

print(ord('a'))
print([10, 20], *[10, 20])
