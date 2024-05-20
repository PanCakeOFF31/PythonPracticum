user = {
    'name': 'maxim',
    'age': 25,
    'gender': 'normal',
    'sex': 'm',
    'cars': [
        'BMW', 'Omoda', 'Lada'
    ]
}

user_name, user_age, user_sex = user['name'], user['age'], user['sex']
print(user_name, user_age, user_sex)

# Порядок и имена ключей не сопоставляются
# cars, gender, *other = user
# print(cars, gender, other)
