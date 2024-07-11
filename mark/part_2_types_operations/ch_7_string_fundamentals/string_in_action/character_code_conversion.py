from helpers import print_section


# character code conversion
def program_1():
    print_section("program_1(): character code conversion")
    letter = "Я"
    code_point = ord(letter)

    print(f'code point of "{letter}" = {code_point}')
    print(f'code point = {code_point}, letter with code point: "{chr(1071)}"')
    # ord() - (ordinal number or code point) of letter
    # chr() - character of (code point or ordinal number)


# character code conversion
program_1()


# get next character
def program_2():
    print_section("program_2(): get next character")

    start_character = 'З'
    next_character = chr(ord(start_character) + 1)

    print(f'start_character = {start_character}')
    print(f'next_character = {next_character}')

    print(chr(1200))
    print(ord('Ұ'))

    print(next(iter([10])))

# get next character
program_2()
