def copy(source, dest):
    with open(source, 'r') as source, open(dest, 'w') as dest:
        dest.write(source.read())

source = str(input()+"text files\A.txt")
dest = str(input()+"text files\B.txt")
copy(source, dest)



#C:\Users\Сакен\Desktop\PP2_2024\lab 6\dir-and-files