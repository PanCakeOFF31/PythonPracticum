def program_1():
    s1 = "Cargo"
    s2 = s1[:]
    s3 = s1[::-1]

    print(s1, s2, s3)
    pass


program_1()


def program_2():
    s = {10, 20, 30}
    for a, b in enumerate(s):
        print(a, b)


program_2()
