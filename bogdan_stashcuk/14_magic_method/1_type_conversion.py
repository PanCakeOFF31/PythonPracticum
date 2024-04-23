title = 'Burgging'
unique_characters = str(set(title))
print(unique_characters)

# Сильная типизация - нельзя смешивать разные типы данных без явности
# print('10' + 5)
# print(10 + '5')

# print(title.__contains__('B'))

bool_value = True
int_val = 7
print(bool_value + int_val, False + int_val)

int_num = 5
float_num = 4.5
print(int_num + float_num)
