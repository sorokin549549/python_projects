# Максимальный в области 2 🌶️
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#   #  #
#   ####
#   #  #
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы диагоналей также учитываются.


n = int(input())
matrix = []


for _ in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

count = matrix[0][0]

for i in range(n):
    for j in range(n):

        if i >= j and i <= n-1-j:
            if matrix[i][j] > count:
                count = matrix[i][j]
        if i <= j and i >= n-1-j:
            if matrix[i][j] > count:
                count = matrix[i][j]
print(count)