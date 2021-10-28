#6. В одномерном массиве найти сумму элементов, находящихся между
#минимальным и максимальным элементами. Сами минимальный и максимальный
#элементы в сумму не включать.

import random

r = [random.randint(0, 99) for _ in range(5)]
print(f'Массив: {r}')

min_ = max_ = sum_ = 0

for item in r:
    if r[item] <= r[min_]:
        min_ = item
    if r[item] >= r[max_]:
        max_ = item

if min_ > max_:
    min_, max_ = max_, min_

for item in range(min_+1, max_):
    sum_ += r[item]

print(f'Исходный массив\n{r}\n\n'
      f'Сумма элементов между минимальным и максимальным значениями равна {sum_}'
      )