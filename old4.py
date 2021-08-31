x = str(input())
z = x.replace('-', '')
if z.isdigit() == False:
    print('NO')
if z.isdigit() == True:
    y = [(i) for i in x.split('-')]
    m = []
    for j in range(0, len(y)):
        m.append(len(y[j]))
    if (m == [1, 3, 3, 4] and int(x[0]) == 7) or m == [3, 3, 4]:
        print('YES')
    else:print('NO')


