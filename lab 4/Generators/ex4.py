def squares():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        yield i * i

for num in squares():
    print(num, end = ",")

print(squares())    
