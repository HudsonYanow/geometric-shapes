import math

class Shape:
    def __init__(self):
        """ initalizes shape"""
        self.area=0
    def calculate_area(self):
        return 0
        
class Square(Shape):
    def __init__(self, sideLength):
        """ initalizes square"""
        self.sideLength = sideLength

    def calculate_area(self):
        """ calculates the area of the square"""
        return self.sideLength*self.sideLength
    
class Rectangle(Shape):
    def __init__(self, width, height):
        """ initalizes rectangle"""
        self.width = width
        self.height = height

    def calculate_area(self):
        """ calculates the area of the rectangle"""
        return self.width*self.height
    
class Circle(Shape):    
    def __init__(self, radius):
        """ initalizes circle"""
        self.radius = radius

    def calculate_area(self):
        """ calculates the area of the circle"""
        return self.radius*self.radius*math.pi
    
class Triangle(Shape):
    def __init__(self, base, height):
        """ initalizes triangle"""
        self.base = base
        self.height = height

    def calculate_area(self):
        """ calculates the area of the triangle"""
        return self.base*self.height/2

square1= Square(4)
rec1=Rectangle(4,8)
circle1=Circle(3)
tri1=Triangle(4,8)

user=input("""what shape would you like to know the area of
           1)square
           2)rectangle
           3)circle
           4)triangle
           """)
if user ==1:
    square1.calculate_area
elif user ==2:
    rec1.calculate_area
elif user ==3:
    circle1.calculate_area
elif user == 4:
    tri1.calculate_area
else:
    print("please input a valid input")
