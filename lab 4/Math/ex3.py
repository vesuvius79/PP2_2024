import math

def area_of_polygon():
    n = int(input())
    l = int(input())
    apothem = l / (2 * math.tan(math.pi / n))
    perimeter = n * l
    k = int(apothem * perimeter / 2)
    return k

print(area_of_polygon())