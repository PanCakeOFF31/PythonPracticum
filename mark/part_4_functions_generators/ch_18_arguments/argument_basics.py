from helpers import print_section


# Simulation  multiple parameters and result
def program_1():
    print_section("program_1(): Simulation  multiple parameters and result")

    def multiply(*m):
        # Неявное создание tuple
        return m[0], m[1], m[0] * m[1]

    x, y, result = multiply(10, 20)
    print(f'Если умножить {x} на {y}, по будет {result}')


# Simulation  multiple parameters and result
program_1()
