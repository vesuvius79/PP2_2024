def isPrime(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt = cnt + 1
    return cnt == 2


list = map(int, input().split())   #Функция split сканирует всю строку и разделяет ее в случае нахождения разделителя.
newlist = [x for x in list if isPrime(int(x))]
print(newlist)