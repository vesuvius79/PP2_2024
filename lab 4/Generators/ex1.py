def squares_generator():
    n = int(input())
    for i in range(1, n+1):
        yield i*i
    
for nums in squares_generator():
    print(nums, end = ",")

print(squares_generator())