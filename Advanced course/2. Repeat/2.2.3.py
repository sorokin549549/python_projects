x = [int(i) for i in input().split()]
for i in range(1, len(x), 2):
    x[i-1], x[i] = x[i], x[i-1]
print(*x)

