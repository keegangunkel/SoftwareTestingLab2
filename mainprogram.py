import problem1, problem2, problem3, problem4, problem5, problem6,problem7, problem8

def main():

    while True:
        print("\nWelcome to my Geometry Program")
        print("1. Sphere \n2. Cylinder\n3. Cone\n4. Cube\n5. Triangle\n6. Trapezoid\n7.Cuboid\n8. Equilateral triangle\n0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 1:
            problem1.main()
        if selection == 2:
            problem2.main()
        if selection == 3:
            problem3.main()
        if selection == 4:
            problem4.main()
        if selection == 5:
            problem5.main()
        if selection == 6:
            problem6.main()
        if selection == 7:
            problem7.main()
        if selection == 8:
            problem8.main()
        if selection == 0:
            break

main()