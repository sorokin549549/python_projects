def cesar_rus(y,x): #функция для кириллицы
    for i in range(0, int(len(x))):
        m = ord(x[i])
        if 1040 <= m <= 1071:   #условие для заглавных букв
            n = m + y
            if n > 1071:
                n = 1039 + (n - 1071)
            v = (chr(n))
            print(v, end='')

        elif 1072 <= m <= 1103:    #условие для строчных букв
            n = m + y
            if n > 1103:
                n = 1071 + (n - 1103)
            v = (chr(n))
            print(v, end='')
        else:
            print(x[i], end='')



def cesar_eng(y,x): #функция для латиницы
    for i in range(0, int(len(x))):
        m = ord(x[i])
        #print(m)
        if 65 <= m <= 90:   #условие для заглавных букв
            n = m + y
            if n > 90:
                n = 64 + (n - 90)
            v = (chr(n))
            print(v, end='')

        elif 97 <= m <= 122:    #условие для строчных букв
            n = m + y
            if n > 122:
                n = 96 + (n - 122)
            v = (chr(n))
            print(v, end='')
        else:
            print(x[i], end='')
y, x = int(input()), input()
cesar_eng(y, x)






