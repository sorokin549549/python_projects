import numpy as np
matrix = []
n = int(input())
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)


x = int(input())

a = np.array(matrix)
result = np.linalg.matrix_power(a, x)

for row in result:
    print(*row)