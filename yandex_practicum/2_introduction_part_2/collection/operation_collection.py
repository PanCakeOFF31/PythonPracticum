# if 10 > 5:
#     print('10 > 5')
#
# if not 5 > 10:
#     print('5 < 10')
#
# if not 5 > 5:
#     print('5 not >  5')

zoo_animals = ['лось', 'слон', 'морж', 'жираф', 'лиса', 'кенгуру', 'панда']
print(zoo_animals)

if 'лиса' in zoo_animals:
    print('В зоопарке есть лиса')

if 'обезьяна' not in zoo_animals:
    print('Обезьяны нет в писке животных')

sleep_list = ['спать', 'дрыхнуть', 'кемарить']
print('Список до добавления нового элемента:', sleep_list)

sleep_list.append('посапывать')
print('Список после добавления нового элемента:', sleep_list)

sleep_set = {'спать', 'дрыхнуть', 'кемарить'}
print('sleep_set', sleep_set)

sleep_set.add('добавка')
print('sleep_set after add the element:', sleep_set)

if 'asd' != 'asdx':
    print()

set_s = {'asd', 'asd,mxzv'}
set({'asd': 10}.keys()).union()
print(set_s)
