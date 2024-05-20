# * operator - unpacking container
digit_list = [1, 2, 3, 4, 5, 6]
name_list = ['max', 'poly', 'andre']

print(digit_list, '->', *digit_list)
print(name_list, '->', *name_list)

total_list = [*digit_list, *name_list]
print(total_list, '->', *total_list)

# ** operator - unpacking dictionary
movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

new_move = {*movie, 'some'}
print(new_move)
new_move = {**movie, 'new_attribute': 'longest'}
print(new_move)

num_1 = 10
num_2 = 330
num_3 = True
*nums, = num_1, num_2, num_3
print(nums, type(nums))
