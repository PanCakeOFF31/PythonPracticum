file = open('unidata.txt', 'w', encoding='utf-8')
file.write('Текстовый файл записали данные')
file.close()

text = open('unidata.txt', 'r', encoding='utf-8')
print(text.read())
print(open('unidata.txt', 'rb').read())
