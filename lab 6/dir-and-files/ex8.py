import os

def delete(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
        else:
            print(f"No write access to {path}. Cannot delete.")
    else:
        print(f"The file {path} does not exist.")


file = str(input()+"\text files\Y.txt")
delete(file)


#C:\Users\Сакен\Desktop\PP2_2024\lab 6\dir-and-files