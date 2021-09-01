from time import *
import random

count = 1
for _ in range(3):

    num = random.randint(0, 1)
    print("Бросок номер", count,':')
    if num == 0:

        print('Орел')
    else:
        print('Решка')
    count += 1

    sleep(3)