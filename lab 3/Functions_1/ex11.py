def palindrome(st):
    s = "".join(reversed(st))
    if s == st:
        print("Palindrome")
        return
    print("Not Palindrome")
    

st = (input())
palindrome(st)  