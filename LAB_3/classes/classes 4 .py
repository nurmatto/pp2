from math import sqrt

class Points:
    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    
    def show(self):
        print((self.x, self.y), (self.x2, self.y2))
        
    def move(self):
        self.x += self.x2
        self.y += self.y2
        print((self.x, self.y))
        
    def distance(self):
        dist = sqrt(pow((self.x2 - self.x), 2) + pow((self.y2 - self.y),2))
        print('Distance between 2 points is equal to', dist)

a, b, c, d = map(int, input("Enter x, y, x2, y2: ").split())

object_1 = Points(a, b, c, d)

object_1.show()
object_1.move()
object_1.distance()
