m = input().replace(' ', '')
n = []
n.append([m[0]])
for i in range(1, len(m)):
    if m[i-1] != m[i]:
        n.append([m[i]])
    elif m[i-1] == m[i]:
        n[-1].extend([m[i]])
print(n)
