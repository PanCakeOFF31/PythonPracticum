# Конвертация других значений в словари
# random = [0, True, 'abc']
random = [['first', 0],
          ['second', True],
          ['third', 'abc'],
          ('tuple', 888)
          ]

random_dict = dict(random)
# random_dict = dict.__init__({1: 2})
print(random_dict)
