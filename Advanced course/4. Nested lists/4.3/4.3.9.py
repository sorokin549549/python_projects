n = int(input())
import math
#math.factorial(4)
c = 0
z = []
for m in range(n):
    c = math.factorial(n)/ (math.factorial(m)*math.factorial(n-m))
    z.append(int(c))
z.append(1)
print(z)