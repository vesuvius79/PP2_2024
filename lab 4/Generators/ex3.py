def divisible_by_3_and_4():
    n = int(input())
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

mylist = []
for num in divisible_by_3_and_4():
    if num != 0:
        mylist.append(num)

    print(mylist)


print(divisible_by_3_and_4())