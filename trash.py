def cesar_eng(x): #функция для латиницы
    for j in range(0, len(x)):

        for i in range(0, (len(x[j]))):
            m = ord(x[j][i])
            #print(m)
            if 65 <= m <= 90:   #условие для заглавных букв
                n = m + len(x[i])
                if n > 90:
                    n = 64 + (n - 90)
                v = (chr(n))
                print(v, end='')
            elif 97 <= m <= 122:    #условие для строчных букв
                n = m + len(x[i])
                if n > 122:
                    n = 96 + (n - 122)
                v = (chr(n))
                print(v, end='')
            else:
                print(x[i], end='')

x = input().split()
cesar_eng(x)