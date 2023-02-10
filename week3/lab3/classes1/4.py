import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def move(self):
        self.x=int(input())
        self.y=int(input())
    def dist(self):
        d=math.sqrt((self.x**2)+(self.y**2))
        print(d)
x=int(input())
y=int(input())
cn=Point(x,y)
cn.dist()
cn.move()
cn.show()
cn.dist()