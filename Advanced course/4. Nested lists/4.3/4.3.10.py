n = int(input())
import math
#math.factorial(4)
c = 0
z = []
for i in range(n):
    z = []
    for m in range(i):
        c = math.factorial(i)/ (math.factorial(m)*math.factorial(i-m))
        z.append(int(c))
    z.append(1)
    print(*z)
