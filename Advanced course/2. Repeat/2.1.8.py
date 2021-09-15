x, y = int(input()), int(input())
z = 0
for i in range(1, x+1):
    z = (z + y) % i
print(z+1)