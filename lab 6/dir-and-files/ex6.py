import string
import os

def generate_text_files(path):
    for letter in string.ascii_uppercase:
        file_name = os.path.join(path, f'{letter}.txt')
        with open(file_name, 'w') as file:
            file.write(f"File {letter}.txt")
dir = str(input())
generate_text_files(dir)



#C:\Users\Сакен\Desktop\PP2_2024\lab 6\dir-and-files