# Write a program to assert the user enters a number greater 9
# than zero

num = int(input("Enter a number: "))

if num > 0:
    print("You entered:", num)
else:
    print("Error: Number must be greater than zero!")
