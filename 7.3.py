n = int(input())
maximum = -1
pre_maximum = -1
for i in range(n):
    num = int(input())    
    if num > maximum:
        pre_maximum = maximum
        maximum = num
    else:
        if pre_maximum < num < maximum:
            pre_maximum = num
print(maximum, pre_maximum, sep='\n')
