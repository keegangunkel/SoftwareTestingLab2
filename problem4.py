####################################################
#
# Keegan Gunkel
#
# Purpose to find volume and surface area of a cube
#
####################################################
import math
def main():
    print("-------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A CUBE")
    print("------------------------------------------------------------- ")
    # User input
    lengthOfCube = eval(input("Please enter the Length of any Side of a Cube: "))
    print()
    # Equations I used
    volume = lengthOfCube**3
    surfaceArea = 6 * lengthOfCube**2
    lateralSurfaceArea= 4 * lengthOfCube**2
    # Prints the answers
    print(" Surface Area of Cube = ", float(surfaceArea))
    print(" Volume of cube = ", float(volume))
    print(" Lateral Surface Area of Cube = ", float(lateralSurfaceArea))
    print("-------------------------------------------------------------")

    
    if __name__ == '__main__':
        main()

