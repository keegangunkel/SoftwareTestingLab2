####################################################
#
# Keegan Gunkel
#
# Purpose to find the area of a trapezoid
#
####################################################
import math

def median():
    pass

def area(base1, base2, height):
    median = (base1 + base2) / 2
    area = (median) * height
    return area

def main():
    print("-------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE AREA OF A TRAPEZOID")
    print("-------------------------------------------------------------")
    base1 = eval(input("Please Enter the base1 :"))
    base2 = eval(input("Please Enter the the base2 :"))
    height = eval(input("Please Enter the height :"))
    median = (base1 + base2) / 2
    area = (median) * height
    print()
    print(" Area of a Trapezoid = ", area)
    print(" Median of a trapezoid = ", median)    
    print("--------------------------------------------------------------")

    if __name__ == '__main__':
        main()