first_list = [1, 2, 3]
second_list = [4, 1, 2]

print(first_list + second_list)
print(first_list.__add__(second_list))

my_dict = {'a': 10,
           'b': 20}
all_values = list(my_dict.keys()) + list(my_dict.values())
print(all_values)


def math_analysis(container: list):
    print('min =', min(container))
    print('max =', max(container))
    print('sum =', sum(container))
    print('avg =', sum(container) / len(container))


math_analysis([10, 20, 5, -4, 0])
