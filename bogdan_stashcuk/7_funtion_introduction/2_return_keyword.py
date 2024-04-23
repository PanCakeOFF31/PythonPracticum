def sum_numbers(a, b):
    sum = a + b
    print(sum)


def sum_nums(a, b):
    return a + b


def sum_none(a, b):
    sum = a + b
    return
    # Unreachable code
    print("Line is not executed")


sum_numbers(10, 5)
sum_numbers(50.5, 20)

nums = sum_nums(sum_nums(10, 5), 100)
print(nums)

print(sum_none(10, 20))
