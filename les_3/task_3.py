#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {r}')

max = r[0]
min = r[0]

for item in r:
    if item > max:
        max = item
    elif item < min:
        min = item
min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив после изменения элементов {min_index} и {max_index}: {r}')
