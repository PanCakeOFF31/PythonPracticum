range_start = 0
range_stop = 18
range_step = 4

r = range(range_start, range_stop, range_step)
print(r, list(r))

for i in [10, 20]:
    print(i)

for i in tuple(r):
    print(i)

print(set(r), list(r))
print(r.step, r.start, r.stop)
print(r.index(12))
