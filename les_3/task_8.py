#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних
#элементов строк. Программа должна вычислять сумму введенных элементов
#каждой строки и записывать в последнюю ячейку строки. В конце следует
#вывести полученную матрицу.

matrix = []

for item in range(4):
    matrix.append([])
    sum = 0
    for n in range(4):
        user_number = int(input(f'Введите элемент {item+1} и {n+1} столбца: '))
        sum += user_number
        matrix[item].append(user_number)

    matrix[item].append(sum)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))