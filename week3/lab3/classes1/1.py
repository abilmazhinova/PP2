class string():
    def __init__(self):
        self.s=""
    def getstring(self):    
        self.s=input()
    def printString(self):
        return self.s.upper()

x = string()
x.getstring()
print(x.printString())

