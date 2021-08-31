n = int(input())
f0 = 1
f1 = 1
fn = 0
print(f1, f0, end=' ')
for i in range(n):
    fn = f1 + f0

    print(fn, end=' ')
    f0 = f1
    f1 = fn

