print(dir())
for name in dir(list):
    print(list.__getattribute__([], name))

