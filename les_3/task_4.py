#4. Определить, какое число в массиве встречается чаще всего.

import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

max_index = 0
for item in r:
    if r.count(max_index) < r.count(item):
        max_index = r.index(item)

print(f'Число {r[max_index]}, встречается {r.count(max_index)} раза')