x = int(input())
m = []
for i in range(x):
    y = input()
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for j in range(len(y)):
        if y[j] == 'a':
            count1 += 1
        if count1> 0 and y[j] == 'n':
            count2 += 1
        if count2>0 and y[j] == 't':
            count3 += 1
        if count3> 0and  y[j] == 'o':
            count4 += 1
        if count4 > 0 and y[j] == 'n':
            count5 += 1
        if count5 > 0:
            m.append(i+1)
            break
print(*m)






