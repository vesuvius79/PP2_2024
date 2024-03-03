import os

def dir_and_files(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)) or os.path.isfile(os.path.join(path, item)):
            print(item)
path = str(input())
dir_and_files(path)


#C:\Users\Сакен\Desktop\PP2_2024\lab 6\dir-and-files