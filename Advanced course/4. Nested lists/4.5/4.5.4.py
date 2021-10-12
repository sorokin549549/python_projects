# Симметричная матрица
# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.


n = int(input())
matrix = []
total = 0
flag = False
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for k in range(n):
    for j in range(n):
        if matrix[k][j] == matrix[j][k]:
            flag = True
        else:
            flag = False
            break



if flag == True:print('YES')
else:print('NO')


