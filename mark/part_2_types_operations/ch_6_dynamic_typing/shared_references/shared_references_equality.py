from helpers import print_section


# same values and references
# comparison by value and reference
def program_1():
    l1 = [1, 2, 3, 4]
    l2 = l1
    l3 = [1, 2, 3, 4]
    print('l1:', l1, 'l2:', l2, 'l3:', l3)
    print('l1 == l2:', l1 == l2, '\nl1 is l2:', l1 is l2, '\nl1 == l3:', l1 == l3, 'l1 is l3:', l1 is l3)

    x1 = 44
    x2 = 44
    print('x1 == x2:', x1 == x2, 'x1 is x2:', x1 is x2)


print_section("same values and references")
print_section("comparison by value and reference")
program_1()
