def area_of_trapezoid():
    h = int(input())
    b1 = int(input())
    b2 = int(input())
    return h * b1 + (b2 - b1) * h / 2


print(area_of_trapezoid())