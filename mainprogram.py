import Cylinder, Cube, Cuboid, Triangle, Trapezoid, Sphere,EquilateralTriangle, Cone

def main():

    while True:
        print("\nWelcome to my Geometry Program")
        print("1. Sphere \n2. Cylinder\n3. Cone\n4. Cube\n5. Triangle\n6. Trapezoid\n7.Cuboid\n8. Equilateral triangle\n0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 1:
            Sphere.main()
        if selection == 2:
            Cylinder.main()
        if selection == 3:
            Cone.main()
        if selection == 4:
            Cube.main()
        if selection == 5:
            Triangle.main()
        if selection == 6:
            Trapezoid.main()
        if selection == 7:
            Cuboid.main()
        if selection == 8:
            EquilateralTriangle.main()
        if selection == 0:
            break

main()