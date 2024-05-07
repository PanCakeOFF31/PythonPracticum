def merge_lists_to_dict(list_1: list, list_2: list) -> dict:
    return dict(zip(list_1, list_2))


list_name = ['maxim', 'pavel', 'vitavel']
list_age = [25, 26, 31]

merged_by_name: dict = merge_lists_to_dict(list_name, list_age)
merged_by_age: dict = merge_lists_to_dict(list_age, list_name)

print(merged_by_name)
print(merged_by_age)
