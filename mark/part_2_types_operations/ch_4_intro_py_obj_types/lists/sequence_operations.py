# срезы над списком - создают новый список
def program_1():
    collection = [123, 'spam', 1.23, True, '😁']
    print('Длина последовательности', collection, 'составляет:', len(collection))
    print('Обращение по индексу:', collection[-1])
    print('Срезы:', collection[:3:1], collection[-1:0:-1])
    print('Все элементы без последнего:', collection[:-1])
    print('Все элементы в обратном порядке:', collection[::-1])


def program_2():
    collection = ['😁', True, 1.23, 'spam', 123]
    print(collection + ['😊', False, 'length'] * 2)
    print(collection)


program_1()
program_2()
