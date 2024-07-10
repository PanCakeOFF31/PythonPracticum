scores = [10, 20, 30, 30, 11, 15, 18, 18]
print('Первый элемент:', next(enumerate(scores)))
scores_ids = [(value, id) for id, value in enumerate(scores)]

for t in scores_ids:
    print(t)

# scores_ids.sort(key=lambda x: x[1], reverse=False)
scores_ids.sort(reverse=False)
print(scores_ids)
print([id for _, id in scores_ids])

print((10, 20) == (10, 20))
print((10, 20) == (20, 10))
print({10, 20} == {10, 20})
print({10, 20} == {20, 10})
