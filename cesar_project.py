y, x = 10, 'Блажен, кто верует, тепло ему на свете!'
for i in range(0, int(len(x))):
    m = ord(x[i])
    #print(m)
    if 1040 <= m <= 1071:
        n = m + y
        if n > 1071:
            n = 1040 + (n - 1071)
        v = (chr(n))
        print(v, end='')

    elif 1072 <= m <= 1103:
        n = m + y
        if n > 1103:
            n = 1072 + (n - 1103)
        v = (chr(n))
        print(v, end='')
    else:
        print(x[i], end='')





