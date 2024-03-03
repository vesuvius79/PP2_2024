def count():
    my_string = str(input())
    cnt1 = sum(1 for i in my_string if i.isupper())
    cnt2 = sum(1 for i in my_string if i.islower())
    return cnt1, cnt2