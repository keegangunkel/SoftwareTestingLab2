import cylinder, cube, cuboid, triangle, trapezoid, sphere,equilateralTriangle, cone

def main():

    while True:
        print("\nWelcome to my Geometry Program")
        print("1. Sphere \n2. Cylinder\n3. Cone\n4. Cube\n5. Triangle\n6. Trapezoid\n7.Cuboid\n8. Equilateral triangle\n0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 1:
            sphere.main()
        if selection == 2:
            cylinder.main()
        if selection == 3:
            cone.main()
        if selection == 4:
            cube.main()
        if selection == 5:
            triangle.main()
        if selection == 6:
            trapezoid.main()
        if selection == 7:
            cuboid.main()
        if selection == 8:
            equilateralTriangle.main()
        if selection == 0:
            break

main()