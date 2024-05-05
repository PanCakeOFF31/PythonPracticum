import datetime as dt

from helpers import *

print_article("Форматирование даты и времени")
print_section()

arrival_time = dt.datetime(2019, 5, 10, 19, 45)
print('Время до форматирования:', arrival_time)
print('Время после форматирования:', arrival_time.strftime('%H:%M'))

print_section_ending()
print_article_ending()
