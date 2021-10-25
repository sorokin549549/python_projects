n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
count = 0
for i in range(n):
    count += 1
    for j in range(m):



        for k in range(j+i-1):
            #
            matrix[i][n - i- 1] = count





for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()