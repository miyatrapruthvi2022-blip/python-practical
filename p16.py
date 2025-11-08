#Create a program to sort tuple with nested tuples 
# Program to sort a tuple containing nested tuples

# Step 1: Create a tuple with nested tuples
d = ((3, 4), (1, 2), (5, 1), (2, 3))

print("Original Tuple:")
print(d)

s = tuple(sorted(d))

print("\nTuple sorted by first element:")
print(s)

s2 = tuple(sorted(d, key=lambda x: x[1]))

print("\nTuple sorted by second element:")
print(s2)
