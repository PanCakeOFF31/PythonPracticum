db_is_available = False

print(db_is_available)
print(type(db_is_available))

db_is_available = True

print(db_is_available)
print(type(db_is_available))


def booling():
    print(bool([]), bool({}), bool(''), bool(0))
    print(bool([1]), bool({1}), bool('1'), bool(-1))
    print(bool(None), bool(not None))


booling()

print(None, not None, [] == [], {} == [], {} == {})
print("abc" == ['a', 'b', 'c'], list("abc") == ['a', 'b', 'c'])
