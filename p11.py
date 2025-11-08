
# Write a python program that asks the user to enter a length in centimeters. 
# If the user enters a negative length, the program should tell the user that the 
# entry is invalid. Otherwise, the program should convert the length to inches and 
# print out the result. (2.54 = 1 inch)  using if

cm = float(input("Enter length in centimeters: "))

if cm < 0:
    print("Invalid entry! Length cannot be negative.")
else:
    # Step 3: Convert to inches (1 inch = 2.54 cm)
   # inches = cm / 2.54
    print("Length in inches:",(cm/2.54))
