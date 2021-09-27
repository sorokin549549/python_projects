def chunked(x,y):
    final = []
    temp = []
    for i in range(len(x)):
        temp.append(x[i])
        if len(temp) == y:
            final.append(temp)
            temp = []
    if len(x) % y != 0:
        final.append(temp)

    print(final)
x, y = (input()).split(), int(input())
chunked(x,y)