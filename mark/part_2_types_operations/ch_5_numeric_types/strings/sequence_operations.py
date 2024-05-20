spam_str = 'super spam'
spam_list = ['s', 'p', 'a', 'm']
print(spam_str, len(spam_str), spam_str[-4])
print(spam_list, len(spam_list), spam_list[0])
# slicing indexing from 0 index to 3 index exclusive with step 1
print(spam_str[0:3:1])
print(spam_str[::2])
# string repeating
print(spam_str * 3)
print(spam_str + ''.join(spam_list))
