x = input().split()
for i in range(0, len(x)):
    print(end=" ")
    count = 0
    for j in range(0, len(x[i])):
        if x[i][j].isalpha() == True:
            count += 1
    for k in range(0, len(x[i])):
        m =ord(x[i][k])
        if 65 <= m <= 90:  # условие для заглавных букв
            n = m + count
            if n > 90:
                n = 64 + (n - 90)
            v = (chr(n))
            print(v, end='')
        elif 97 <= m <= 122:  # условие для строчных букв
            n = m + count
            if n > 122:
                n = 96 + (n - 122)
            v = (chr(n))
            print(v, end='')
        else:
            print(x[i][j], end='')