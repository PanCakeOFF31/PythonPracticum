from helpers import *

print_article('Поднможества и супермножества')
print_section()

subset = {10, 5, 35}
superset = {20, 5, 44, 10, 77, 35}

print('Супер множество:', superset)
print('Под множество:', subset)

print('subset является подмножеством superset:', subset.issubset(superset))
print(subset.issuperset(superset))

print('superset является супер множеством subset', superset.issuperset(subset))
print(subset.issuperset(superset))

print_section_ending()
print_section('Простое уточнение по поводу под/супер/множеств')

s = {10, 20}
ss = {10, 20}

print(s.issubset(ss), s.issuperset(ss))

print_subsection()
print_article_ending()
