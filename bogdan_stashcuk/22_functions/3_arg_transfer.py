from helpers import print_article


def fn_immut(a: int, b: int):
    print(a, id(a), b, id(b))


def fn_mutt(container: set):
    container.add("ἋἊἃ")
    print(container, id(container))


print_article("Передача immutable argument")

num_1 = 10
num_2 = 100

fn_immut(num_1, num_2)
print(num_1, id(num_1), num_2, id(num_2))

print_article("Передача mutable argument")

container: set = {10, "😊", True, None}
print(container, id(container))
fn_mutt(container)
