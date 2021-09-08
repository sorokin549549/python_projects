x = input().split()

y = []
for i in range(len(x)):
    y.append(x[i-1])
print(*y)