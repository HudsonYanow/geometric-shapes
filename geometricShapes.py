import math

class Shape:
    def __init__(self):
        """
        initiates the shape class
        """
        self.area=0
    def calculate_area(self):
        return 0
        
class Square(Shape):
    def __init__(self, sideLength):
        self.sideLength = sideLength

    def calculate_area(self):
        return self.sideLength*self.sideLength
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height
    
class Circle(Shape):    
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius*self.radius*math.pi
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base*self.height/2
shapesList=[]
square1= Square(4)
rec1=Rectangle(4,8)
circle1=Circle(3)
tri1=Triangle(4,8)
shapesList.append(square1)
shapesList.append(rec1)
shapesList.append(circle1)
shapesList.append(tri1)
for curShape in shapesList:
    print(curShape.calculate_area())