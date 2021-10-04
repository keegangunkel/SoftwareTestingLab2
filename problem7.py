####################################################
#
# Keegan Gunkel
#
# Purpose to find the area of a trapezoid
#
####################################################
import math
def main():
    print("---------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A CUBOID")
    print("---------------------------------------------------------------")
    length = eval(input("Please Enter the length :"))
    width = eval(input("Please Enter the the width :"))
    height = eval(input("Please Enter the height :"))
    surfaceArea = (2*length*width)+(2*length*height)+(2*height*width)
    volume = length*width*height
    lateralSurfaceArea = 2*(length + width)* height
    print()
    print("The Surface Area of a Cuboid = ", float(surfaceArea))
    print("The Volume of a Cuboid = ",float(volume))
    print("The lateral Surface Area of a Cuboid = ", float(lateralSurfaceArea))
    print("---------------------------------------------------------------")

    if __name__ == '__main__':
        main()