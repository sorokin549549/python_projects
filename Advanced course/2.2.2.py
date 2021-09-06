x = (input()).split()
y = []
for i in range(len(x)-1):
    if int(x[i]) < int(x[i+1]):
        y.append(x[i])
print((len(y)))
