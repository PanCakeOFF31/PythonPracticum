def merge_lists_to_dict(**kwargs) -> dict:
    return dict(zip(kwargs['list_1'], kwargs['list_2']))


list_name = ['maxim', 'pavel', 'vitavel']
list_age = [25, 26, 31]

merged_by_name: dict = merge_lists_to_dict(list_1=list_name, list_2=list_age)
merged_by_age: dict = merge_lists_to_dict(list_1=list_age, list_2=list_name)

print(merged_by_name)
print(merged_by_age)


def update_car_info(**kwargs):
    kwargs['is_available'] = True
    return kwargs


updated_car = update_car_info(engine='big', volume=1.5, color='weight')
print(updated_car)
