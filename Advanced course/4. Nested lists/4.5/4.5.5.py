# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
for k in range(n):
    matrix[k][k], matrix[n - k - 1][k] = matrix[n - k - 1][k], matrix[k][k]
for o in range(n):
    for l in range(n):
        print(matrix[o][l], end=' ')
    print()