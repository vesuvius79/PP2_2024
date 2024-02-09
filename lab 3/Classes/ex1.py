class Student():
    def __init__(self):
        pass
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
        
p1 = Student()     
p1.getString()
p1.printString()