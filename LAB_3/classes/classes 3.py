class Shape:
    def __init__(self,length):
        self.length=length
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def area(self):
        print(self.length**2)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.width=width
        super().__init__(length)
    def area(self):
        print(self.length*self.width)
length=int(input())
width=int(input())
object_1=Rectangle(length, width)
object_1.area()