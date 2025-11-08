#Write a python program that asks the user to enter a length in
#centimeters. If the user enters a negative length, the program
#should tell the user that the entry is invalid. Otherwise, the
#program should convert the length to inches and print out the
#result. (2.54 = 1 inch)
import math   # for math.pi

while True:
    print("\n=== MENU ===")
    print("1. Find Area of Circle")
    print("2. Find Area of Triangle")
    print("3. Find Area of Square")
    print("4. Find Simple Interest")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        r = float(input("Enter radius of circle: "))
        area = math.pi * r * r
        print("Area of Circle =", area)

    elif choice == 2:
        b = float(input("Enter base of triangle: "))
        h = float(input("Enter height of triangle: "))
        area = 0.5 * b * h
        print("Area of Triangle =", area)

    elif choice == 3:
        side = float(input("Enter side of square: "))
        area = side * side
        print("Area of Square =", area)

    elif choice == 4:
        p = float(input("Enter Principal: "))
        r = float(input("Enter Rate of Interest: "))
        t = float(input("Enter Time (in years): "))
        si = (p * r * t) / 100
        print("Simple Interest =", si)

    elif choice == 5:
        print("Exiting Program... Goodbye! 👋")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

