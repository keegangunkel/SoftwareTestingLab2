####################################################
#
# Keegan Gunkel
#
# Purpose to find the area of a triangle
#
####################################################
import math

def perimeter():
    pass

def area(firstSide, secondSide, thirdSide):
    perimeter = firstSide + secondSide + thirdSide
    semiPerimeter = perimeter/2
    triangleVar = round(semiPerimeter*(semiPerimeter - firstSide)*(semiPerimeter - secondSide)*(semiPerimeter - thirdSide), 2)
    area = math.sqrt(triangleVar)
    return area

def main():
    print("-------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE AREA OF A TRIANGLE")
    print("-------------------------------------------------------------")
    firstSide = eval(input("Please Enter the First Side of a Triangle: "))
    secondSide = eval(input("Please Enter the Second Side of a Triangle: "))
    thirdSide= eval(input("Please Enter the Third Side of a Triangle: "))
    perimeter = firstSide + secondSide + thirdSide
    semiPerimeter = perimeter/2
    triangleVar = round(semiPerimeter*(semiPerimeter - firstSide)*(semiPerimeter - secondSide)*(semiPerimeter - thirdSide), 2)
    area = math.sqrt(triangleVar)
    print()
    print(" The Perimeter of Triangle = ", perimeter)
    print(" The Semi perimeter of Triangle = ", semiPerimeter)
    print(" The Area of a Triangle is ", area)
    print("-------------------------------------------------------------")

    if __name__ == '__main__':
        main()