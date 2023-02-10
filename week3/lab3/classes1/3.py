class Shape():
    area=0
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length * self.width
        print(area)

length=int(input())
width=int(input())
x=Rectangle(length,width)
x.area()