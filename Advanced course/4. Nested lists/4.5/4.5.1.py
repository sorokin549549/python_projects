# Таблица умножения
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
#
# Формат входных данных
# На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 33 символа (для этого используйте строковый метод ljust()).

n,m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(i * j)
    matrix.append(row)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()