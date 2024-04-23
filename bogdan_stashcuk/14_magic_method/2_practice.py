def int_float_multiplication():
    int_num = 50
    float_num = 7.5

    print(int_num * float_num)

    print(int_num.__mul__(float_num))
    # print(int_num.__mul__('asd')) #  NotImplemented
    print(float_num.__rmul__(int_num))
    print(float_num.__mul__(int_num))


# int_float_multiplication()


def int_str_mul(number, string):
    return number * string


print(int_str_mul(3, 'Max'))
print(str.__mul__('Min', 5))
# str.__rmul__()
