#class Shape:
#   def __init__(self, length):
#       self.length=length
#   def area(self):
#       print(self.length**2)
#       return 0
#class Square(Shape):
#   def __init__(self, length):
#       super().__init__(length)
#       self.length=length
#   def area(self):
#       print(self.length*self.length)
#x=Shape(5)
#y=Square(5)
#y.area()
#x.area()


#or we can do it like this:


#class Shape:
#   def __init__(self, length):
#       self.l=length
#   def area(self):
#       print(self.l**2)
#class Square(Shape):
#   def __init__(self, length):
#       super().__init__(length)
#
#a=int(input())
#obj=Square(a)
#obj.area()
#   

# or this way :
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length=length
        
    def area(self):
        print(self.length**2)
ob_1=Shape()
print('by default', ob_1.area())
a=int(input())
ob_2=Square(a)
ob_2.area()