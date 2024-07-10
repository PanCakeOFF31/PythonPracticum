# Находит максимальную сумму префиксов
# O(n^2)
def get_max_prefix_sum(arr) -> int:
    maximal_sum = 0

    for i in range(1, len(arr) + 1):
        current_sum = sum(arr[:i])
        maximal_sum = max(maximal_sum, current_sum)

    return maximal_sum


print(get_max_prefix_sum([1, 0, 0, -1]))

# range - не включает, splice - не включает последний элемент
arr = [i for i in range(10)]
print(arr, 'length:', len(arr))

for i in range(1, len(arr) + 1):
    print(arr[:i])
