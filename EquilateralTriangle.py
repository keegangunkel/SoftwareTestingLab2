####################################################
#
# Keegan Gunkel
#
# Purpose to find the area of an equilateral triangle
#
####################################################
import math
def main():
    print("---------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE AREA OF AN EQUILATERAL TRIANGLE")
    print("---------------------------------------------------------------")
    length = eval(input("Please Enter Length of any Equilateral Triangle: "))
    area = (math.sqrt(3)/4)*length**2
    perimeter = length*3
    seimPerimeter = perimeter/2
    altitude = length*math.sqrt(3)*.5
    print()
    print(" Area of Equilateral triangle = ", round(area, 2))
    print(" Perimeter of Equilateral Triangle = ",round(perimeter, 2))
    print(" Semi Perimeter of Equilateral Triangle = ",round(seimPerimeter,2))
    print(" Altitude of Equilateral Triangle = ",round(altitude, 2))
    print("----------------------------------------------------------------")

    if __name__ == '__main__':
        main()