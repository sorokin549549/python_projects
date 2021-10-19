# Магический квадрат 🌶️
# Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n
# 2
#   так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
x =[]
count = 0
for j in range(n):
    for i in range(n):
        x.append(matrix[j][i])
for j in range(1, ((n*n)+1)):
    if j in x:
        count += 1
if count == n*n:
    summa_diagomal = 0
    summa_diagomal1 = 0
    for i in range(n):
        summa_diagomal += matrix[i][i]
        summa_diagomal1 += matrix[i][n - i - 1]
    for i in range(n):
        bok_goriz = 0
        bok_vert = 0
        for j in range(n):
            bok_goriz += matrix[i][j]
            bok_vert += matrix[j][i]
    if bok_vert == bok_goriz == summa_diagomal == summa_diagomal1:
        print('YES')
    else:
        print('NO')
else:print('NO')
