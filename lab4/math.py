import math
#1
def convert():
    degree = int(input('Input degree: '))
    print('Output radian: {}'.format(degree/180*math.pi))
#2
def trapezoid_area():    
    h = int(input("Height: "))
    a = int(input('Base, first value: '))
    b = int(input('Base, second value: '))
    print((a+b)/2*h)
#3
def regular_polygon_area():
    sides = int(input("Sides: "))
    length_of_side = int(input("Length of side: "))
    p_area = sides * (length_of_side ** 2) / (4 * math.tan(math.pi / sides))
    print("Area of regular polygon is: ", p_area)
#4
def parallelogram_area():
    length = int(input("Length of parallelogram: "))
    height = int(input("Height: "))
    area = length * height
    print("Area: ", area)