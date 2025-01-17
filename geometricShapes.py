import math
import BL

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




active=True
while active:
    user=BL.intInputValidator("""what shape would you like to know the area of
            1)square
            2)rectangle
            3)circle
            4)triangle
            0)exit
            """, "please input a valid number from 0-4")
    if user == 1:
        len=BL.intInputValidator("what is the length of each side of the square: ", "please input a number")
        square1= Square(len)
        print(f"the area of the square is {square1.calculate_area()}")
    elif user ==2:
        wid=BL.intInputValidator("what is the width of the rectangle: ", "please input a number")
        height=BL.intInputValidator("what is the height of the rectangle: ", "please input a number")
        rec1 = Rectangle(wid, height)
        print(f"the area of the rectangle is {rec1.calculate_area()}")
    elif user ==3:
        rad=BL.intInputValidator("what is the radius of the circle: ", "please input a number")
        circle1=Circle(rad)
        print(f"the area of the circle is {circle1.calculate_area()}")
    elif user == 4:
        bas=BL.intInputValidator("what is the length of the base of the triangle: ", "please input a number")
        hei=BL.intInputValidator("what is the height of the triangle: ", "please input a number")
        tri1=Triangle(bas, hei)
        print(f"the area of the triangle is {tri1.calculate_area()}")
    elif user == 0:
        exit()
    else:
        print("please input a valid input")
