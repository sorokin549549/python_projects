# Напишите программу для вычисления суммы двух матриц.
#
# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

n, m = [int(i) for i in input().split()]
matrix1 = list()
matrix2 = list()
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix1.append(temp)
input()
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix2.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix1[i][j]+matrix2[i][j], end=' ')
    print()
