def isPalindrome():
    my_string = str(input())
    rev_string = ''.join(reversed(my_string))
    if my_string == rev_string:
        print("This string is a palindrome!")
    else:
        print("This string is not a palindrome!")
        return

isPalindrome()