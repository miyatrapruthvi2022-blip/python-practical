# Write a program to create nested list and display its elements. 
nl = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Nested List:", nl)

print("\nElements of Nested List:")
for i in nl:
    for j in i:
        print(j, end=" ")
    print()   
