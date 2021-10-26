n, m = [int(i) for i in input().split()]
#
matrix = [[0] * m for _ in range(n)]

x = 1
high = m - 1
low = 0
count = int((n+1)/2)


for i in range(count):
    for j in range(low, high+1):
        matrix[i][j] = x
        x+=1
    for j in range(low+1, high+1):
        matrix[j][high] = x
        x+=1
    for j in range(high-1, low-1, -1):
        matrix[high][j] = x
        x+=1
    for j in range(high-1, low, -1):
        matrix[j][low] = x
        x+=1
    low = low+1
    high =high-1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()