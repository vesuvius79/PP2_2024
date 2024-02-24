def from_n_to_0():
    n = int(input())
    for i in range(n, -1, -1):
        yield i

for num in from_n_to_0():
    print(num, end = ",")

print(from_n_to_0())