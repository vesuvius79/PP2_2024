import os

def lines(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file = str(input())
line = lines(file)
print(line)


#C:\Users\Сакен\Desktop\PP2_2024\lab 6\dir-and-files