import math
def get_area_circle(radius):
    """Calculate the area of a circle given its radius"""
    area = 0
    area = math.pi * radius **2 #πr2
    return area
def get_circumference(radius1):
        """Calculate the circumference of a circle given its radius"""
        circumference = 2 * math.pi * radius1
        return circumference
def get_area_square(side):
    """Calculate the area of a square given its side length"""
    area = side ** 2
    return area
def get_area_triangle(base, height):
    """Calculate the area of a triangle given its base and height"""
    area = 0.5 * base * height
    return area

print('Area of the circle is',get_area_circle(2))
print('circumference of the circle is',get_circumference(5))
print('Area of square',get_area_square(4))
print('Area of square',get_area_triangle(1.0, 1.0))
