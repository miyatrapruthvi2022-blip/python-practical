#Create a program to display memory locations of two variables using id() function, and then use identity
#operators two compare whether two objects are same or not.

a = [10,8,90]
b = [10,8,90]

print("Memory location of a:", id(a))
print("Memory location of b:", id(b))

print("a is b:", a is b)
print("a is not b:", a is not b)
