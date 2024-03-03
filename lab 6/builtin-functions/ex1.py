from functools import reduce
def multiple():
    my_list = list(input())
    result = reduce(lambda x,y: x*y, my_list)
    return result