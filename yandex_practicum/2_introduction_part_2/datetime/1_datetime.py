import datetime as dt

from helpers import *

print_article('Работа со временем')
print_section('datetime()')
print_subsection('Конструктор класса')

start_time = dt.datetime(2024,
                         5,
                         24,
                         7,
                         59,
                         30)
# start_time = dt.datetime.__new__()
print(start_time)

print_subsection_ending()
print_subsection('Арифметические операции со временем')

start_time = dt.datetime(2024,
                         5,
                         24)
end_time = dt.datetime(2024, 5, 25, minute=25)

print('difference:', start_time - end_time)
print('difference:', end_time - start_time)
print(start_time.date(), start_time.time(), start_time.astimezone())

print_subsection_ending()
print_subsection('UTC')

now = dt.datetime.now()
print(now, 'dt.datetime.utcnow()', dt.UTC)
# Получаем московское время от UTC
period = dt.timedelta(hours=3)
print('Сумма datetime + timedelta:', dt.datetime.utcnow() + period)
print('Сумма datetime + timedelta:', dt.datetime.utcnow().__sub__(period))
print('Правильное получение времени:', dt.datetime.now(dt.timezone.utc))

print_subsection_ending()
print_section_ending()
print_article_ending()
