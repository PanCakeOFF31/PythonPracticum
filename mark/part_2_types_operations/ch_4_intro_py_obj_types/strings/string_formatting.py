value1 = "March, May"
value2 = "June, July"

# formatting expression
format_type_1 = "%s, ...., %s" % (value1, value2)
# formatting
format_type_2 = "{}, ..., {}".format(value1, value2)
# formatting
format_type_3 = "{1}, ..., {0}".format(value2, value1)

print(format_type_1)
print(format_type_2)
print(format_type_3)

# Форматирование для type_2 с указанием символов после запятой
value3 = "{:,.5f}".format(244.5123549)
print(value3)
del value3

# Форматирование для type_1 с указанием символов после запятой
value3 = "%.2f" % (244.5123542)
print(value3)
