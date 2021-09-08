#x = [int(i) for i in input().split()]
y = int(input())
z = []
for i in range(y):
    z.append(int(input()))
x = int(input())
flag = False
for j in range(len(z)):
    if z[j] == 0:
        continue
    if x / z[j] in z[j+1:]:
        flag = True
if flag == False:print('НЕТ')
else:print('ДА')



