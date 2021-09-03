m,r = float(input()), float(input())
x = m / (r*r)
#print(x)
if 18.5 <= x <= 25:
    print('Оптимальная масса')
if 18 > x:
    print('Недостаточная масса')
if x > 25:
    print('Избыточная масса')

