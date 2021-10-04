####################################################
#
# Keegan Gunkel
#
# Purpose to find volume and surface area of a cone
#
####################################################
import math
def main():
    print("-------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A CONE")
    print("-------------------------------------------------------------")
    # User input
    radius= eval(input("Please enter the radius of a cone: "))
    height= eval(input("Please enter the height of a cone: "))
    print()
    # Eqautions to figure out problem
    surfaceArea = math.pi * radius * (radius + math.sqrt (height**2 + radius**2))
    volume = math.pi * radius**2 * height/3
    lateralSurfaceArea = math.pi * radius * math.sqrt (height**2 + radius**2)
    sideSlantLength = math.sqrt (radius**2 + height**2) 
    # Printing answers and rounding them
    print("Length of side (slant) of the cone = ",round(sideSlantLength, 2))
    print("The surface Area of the cone = ",round(surfaceArea, 2))
    print("The volume of the cone = ",round(volume, 2))
    print("Lateral surface area of the cube = ",round(lateralSurfaceArea, 2))

    if __name__ == '__main__':
        main()