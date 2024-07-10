from helpers import print_section


# Intersecting
def program_1():
    print_section("program_1(): Intersecting")

    # можно переделать в list comprehension
    # Первый аргумент seq1 - обязан поддерживать цикл for
    # Второй аргумент seq2 - обязан поддерживать оператор in
    def intersect(seq1, seq2):
        res = []
        for item in seq1:
            if item in seq2 and item not in res:
                res.append(item)
        return res

    print(intersect('maxim', 'maximum'))
    print(intersect('max', 'minimum'))
    print(intersect('tree', 'treeper'))

    word_1 = 'tree'
    word_2 = 'treeper'
    print([item for item in word_1 if item in word_2])

    # Демонстрация полиморфизма
    print(intersect([10, 20, 30], (20, 30, 50)))

    pass


# Intersecting
program_1()
