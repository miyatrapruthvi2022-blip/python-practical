# Write a program to search an element in the list usingfor loop and also demonstrate the use of 
# “else” with for loop.

# Step 1: Create a list
numbers = [10, 20, 30, 40, 50]

# Step 2: Take element to search
search = int(input("Enter number to search: "))

# Step 3: Search using for loop
for num in numbers:
    if num == search:
        print(search, "found in the list!")
        break
else:
    print(search, "not found in the list.")
