import math

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class circle(Shape):

        def __init__(self, radius):
            self.radius = radius


        def area(self):  

            return math.pi * self.radius ** 2
        

        def perimeter(self):
            return 2 * math.pi * self.radius
        
        
class Rectangle(Shape):

        def __init__(self, width, length):
            self.width = width
            self.length = length      

        def __eq__(self, other):
             if not isinstance(other, Rectangle):
                 return False
             return self.width == other.width and self.length == other.length
             

        def area(self):
             return self.width * self.length


        def perimeter(self):
            return 2 * (self.width + self.length)   


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
                     