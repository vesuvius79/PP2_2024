def rev(s):
    for i in range(len(s)-1, -1, -1):
        print(s[i], end=' ')

s=input().split()
rev(s)