def evens():
    n = int(input())
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

for even in evens():
    if even != 0:
        print(even, sep=", ")


print(evens())