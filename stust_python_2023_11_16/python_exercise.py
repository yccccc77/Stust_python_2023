import math
class MyShape:
    def __init__(self,side=None, length=None,width=None,radius=None):
        self.side=side
        self.length=length
        self.width=width
        self.radius=radius
    
    def getSquareArea(self):
        if self.side is not None:
            return self.side ** 2
        else:
            return None

    def getRectangleArea(self):
        if self.length is not None and self.width is not None:
            return self.length * self.width
        else:
            return None

    def getCircleArea(self):
        if self.radius is not None:
            return math.pi * (self.radius ** 2)
        else:
            return None

shape1 = MyShape(side=5)
print(f"Square Area: {shape1.getSquareArea()}")

shape2 = MyShape(length=4, width=6)
print(f"Rectangle Area: {shape2.getRectangleArea()}")

shape3 = MyShape(radius=3)
print(f"Circle Area: {shape3.getCircleArea()}")
