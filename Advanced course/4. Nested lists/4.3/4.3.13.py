def chunked(podpiski):
    final = [[]]
    for i in range(1, len(podpiski) + 1):
        for j in range(0, (len(podpiski) + 1) - i):
            final.append(podpiski[j:j + i])
    print(final)


x = input().split()
chunked(x)
