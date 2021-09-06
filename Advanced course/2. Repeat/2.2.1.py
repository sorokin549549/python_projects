x = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(x):
    a,b = map(int, input().split())
    if a > 0 and b > 0:
        count1 += 1
    if a < 0 and b > 0:
        count2 += 1
    if a < 0 and b < 0:
        count3 += 1
    if a > 0 and b < 0:
        count4 += 1
print('Первая четверть:', count1)
print('Вторая четверть:', count2)
print('Третья четверть:', count3)
print('Четвертая четверть:', count4)