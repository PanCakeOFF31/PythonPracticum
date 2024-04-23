def immutable():
    var_1 = 100
    var_2 = var_1
    var_2 = var_1 + 99

    print(var_1, var_2)


def mutable():
    var_1 = ['Long', 'Width']
    var_2 = var_1
    var_2.append('Fast')

    print(var_1, var_2)


immutable()
mutable()
