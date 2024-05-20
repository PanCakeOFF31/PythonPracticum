# dictionary - definition
d = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(d)
# fetching value by key 'quantity'
print(d['quantity'], d.__getitem__('quantity'))
# modifying value by key
d['quantity'] += 10
print(d)
# bob
bob1 = dict(name='Bob', job='developer', age=40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'developer', 40]))
print(bob2)
