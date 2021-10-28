#7. В одномерном массиве целых чисел определить два наименьших элемента.
#Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for item in r:
    if r[min_index_1] > item:
        min_index_2 = min_index_1
        min_index_1 = r.index(item)
    elif r[min_index_2] > item:
        min_index_2 = r.index(item)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')