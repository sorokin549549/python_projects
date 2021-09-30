n,m = int(input()), int(input())
matrix = list()

for _ in range(n):
    row = list()
    for _ in range(m):
        row.append(input())
    matrix.append(row)
for item in matrix:
    print(' '.join(item))