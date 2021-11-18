# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа mm и kk — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

import numpy
n, m = [int(i) for i in input().split()]
first_matrix = list()
second_matrix = list()


for i in range(n):
    temp = [int(num) for num in input().split()]
    first_matrix.append(temp)
input()
f, y = [int(i) for i in input().split()]
for i in range(f):
    temp = [int(num) for num in input().split()]
    second_matrix.append(temp)

a = numpy.array(first_matrix)
b = numpy.array(second_matrix)
total = a.dot(b)
for row in total:
    print(*row)

