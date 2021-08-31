num = int(input())
last_digit = num % 10
xmin = last_digit
xmax = last_digit

while num != 0:

    last_digit = num % 10
    if  last_digit > xmax:
        xmax = last_digit
        #print(xmin, 'if', xmax, last_digit)
    else:
        if last_digit < xmin:
           xmin = last_digit
           #print(xmin, 'else', xmax, last_digit)
    num = num // 10
if xmax == xmin:
    print('YES')
else:print('NO')
