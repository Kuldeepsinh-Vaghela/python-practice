
# Define a class named Shape and its subclass Square. The Square
# class has an init function which takes length as argument. Both
# classes have an area function which can print the area of the
# shape where Shape’s area is 0 by default.

class Shape:
    def __init__(self,color):
        self.color = color
    
    def area(self):
        return '0'

class Square(Shape):
    def __init__(self,color,length):
        super().__init__(color)
        self.length = length
    
    def area(self):
        return self.length * self.length


shp = Shape('blue')
sqr = Square('black',10)

print(f"The area of square is {sqr.area()}")
print(f"The area of shape is {shp.area()}")
print(f"The color of shape is {shp.color}")
print(f"The color of square is {sqr.color}")

