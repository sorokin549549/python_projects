# Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for i in list1:
    counter += len(i)
for j in range(len(list1)):
    total += (sum(list1[j]))
print(total/counter)
