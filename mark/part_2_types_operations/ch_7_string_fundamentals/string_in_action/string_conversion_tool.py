from helpers import print_section


# String Conversion
def program_1():
    print_section("program_1(): String Conversion")
    # print("42" + 1)
    # print(1 + "1")
    print(int("42"), str(1))
    print(repr(int("42")), repr(str(1)))

    float_as_text = "1.234E-10"
    print(float(float_as_text), repr(float(float_as_text)))


# String Conversion
program_1()
