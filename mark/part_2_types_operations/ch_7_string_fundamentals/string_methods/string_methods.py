import helpers
from helpers import print_section


# Изменения части строки
def program_1():
    print_section("program_1(): Изменения части строки")
    original = 'spammy'

    helpers.log("Замена через срез и конкатенацию")
    sliced = original[:3] + 'xx' + original[5:]
    print(original, sliced)

    helpers.log("Замена через .replace()")
    replaced = original.replace('mm', 'xx', 1)
    print(original, replaced)


# Изменения части строки
program_1()


# replace method
def program_2():
    print_section("program_2(): replace method")
    original = 'aa&bb&cc&dd'''
    symbol = '&'
    replace_chr = '_SPAM_'

    print(f'original: {original}')
    print(f'replace one time: {original.replace(symbol, replace_chr, 1)}')
    print(f'replace two times: {original.replace(symbol, replace_chr, 2)}')
    print(f'replace default: {original.replace(symbol, replace_chr)}')


# replace method
program_2()


# converting to mutable collection and back
def program_3():
    print_section("program_3(): converting to mutable collection and back")

    original = "spammy_" * 10
    mutable = list(original)
    result = ''.join(mutable)
    print(original, mutable, result)


# converting to mutable collection and back
program_3()
