x = input().split()
y = []

for i in range(len(x)):
    #print(x[i])
    if x[i] not in y:
        y.append(x[i])


print(len(y))
