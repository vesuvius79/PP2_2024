def write(path, data):
    with open(path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file = str(input())
data = [23,24]
write(file, data)


#C:\Users\Сакен\Desktop\PP2_2024\lab 6\dir-and-files