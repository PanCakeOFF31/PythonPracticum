# Механизм спискового включения
nums = [10, 11, 12, 13, 7, -5, 0, -22, 14, -3, -5, -2]
sq = [num ** 2 for num in nums]
print(nums, '->', sq)
# фильтрация с преобразованием
filtered = [[num, num ** 2] for num in nums if num < 0 and num % 2 == 0]
print(filtered)
#
spam = 'sPaMs'
spams = [character * 2 for character in spam]
print(spam, '->', spams, '->', ''.join(spams))

# generator of list
generator = (num for num in range(0, 100, 20))
print(next(generator), next(generator), next(generator), next(generator))
# generator of set
nums_set = {n for n in range(0, 100, 20)}
print(nums_set)
# generator of dict
nums_dict = {n: 'text' for n in range(0, 100, 20)}
print(nums_dict)
