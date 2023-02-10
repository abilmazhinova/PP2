class Shape():
    area=0
    def area(self):
        pass

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        area=self.length**2
        print(area)
length=int(input())
cn=Square(length)
cn.area()
