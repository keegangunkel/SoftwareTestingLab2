####################################################
#
# Keegan Gunkel
#
# Purpose to find the area of a trapezoid
#
####################################################
import math
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
    print(" Area of a Trapezoid = ", round(area,  2))
    print(" Median of a trapezoid = ", round(median, 2))    
    print("--------------------------------------------------------------")

    if __name__ == '__main__':
        main()