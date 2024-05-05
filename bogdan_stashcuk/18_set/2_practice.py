from helpers import *

print_article()

f_list = [11, 12, 13]
s_list = [10, 20, 30]
string = 'something'

# Нельзя в множество добавлять изменяемые объекты - unhashable
# result_set = {f_list, s_list, string}
result_set = {tuple(f_list), tuple(s_list), string}
print(result_set)

print_article_ending()
