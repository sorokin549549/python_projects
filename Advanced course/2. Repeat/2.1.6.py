x = (input())
y = x[-5:]
z = x[:(len(x)-5)]
if len(x) <= 5:
    print(int(y[::-1]))
else:
    print(z+(y[::-1]))
#print(z)
#print(y)