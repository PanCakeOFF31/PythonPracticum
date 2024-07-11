x = 99


def global_1():
    global x
    x += 1


def global_2():
    import other_globals
    other_globals.x += 1


def global_3():
    import sys
    this_module = sys.modules['other_globals']
    this_module.x += 1

#
# print(x)
#
# global_1()
# print(x)

# global_2()
# print(x)
