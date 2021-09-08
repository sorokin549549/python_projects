x = input()
count1 = 0
count2 = 0
countmax = 0
for i in range(len(x)):

    if x[i] == 'Р':
        count1 += 1
        if count1 > countmax:
            countmax = count1

    elif x[i] == 'О':
        count1 = 0


print(countmax)

#ppc ya loh
# s = input().split('О')
# print(len(max(s)))