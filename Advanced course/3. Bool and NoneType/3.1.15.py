# объявление функции
def func(num1, num2):
    return num2 % num1 == 0

# считываем данные
num2, num1 = int(input()), int(input())


if func(num1, num2):
    print('делится')
else:
    print('не делится')