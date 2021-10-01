n,m = int(input()), int(input())
matrix = list()

for _ in range(n):
    row = list()
    for _ in range(m):
        row.append(input())
    matrix.append(row)
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
print()
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()