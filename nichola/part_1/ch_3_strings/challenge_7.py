normal_word = input("Enter standard word: ")

vowels = ('a', 'e', 'i', 'o', 'u')

first_letter = normal_word[0]
rest = normal_word[1:]

if first_letter in vowels:
    latin_word = normal_word + 'way'
else:
    latin_word = rest + first_letter + 'ay'

print(latin_word)

# так как строка позиционно упорядоченная коллекция - можно получать подсписок с конца к началу
print(normal_word[-1::-1])
