####################################################
#
# Keegan Gunkel
#
# Purpose to find the area of an equilateral triangle
#
####################################################
import math

def perimeter():
    pass

def area(length):
    area = (math.sqrt(3)/4)*length**2
    return area

def main():
    print("---------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE AREA OF AN EQUILATERAL TRIANGLE")
    print("---------------------------------------------------------------")
    length = eval(input("Please Enter Length of any Equilateral Triangle: "))
    area = (math.sqrt(3)/4)*length**2
    perimeter = length*3
    semiPerimeter = perimeter/2
    altitude = length*math.sqrt(3)*.5
    print()
    print(" Area of Equilateral triangle = ", area)
    print(" Perimeter of Equilateral Triangle = ", perimeter)
    print(" Semi Perimeter of Equilateral Triangle = ",semiPerimeter)
    print(" Altitude of Equilateral Triangle = ", altitude)
    print("----------------------------------------------------------------")

    if __name__ == '__main__':
        main()