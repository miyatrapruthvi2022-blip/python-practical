# Write a program to accept elements in the form of a tuple and display its 
# minimum, maximum, sum and average. 

e= input("Enter numbers separated by spaces: ")

num = tuple(map(int, e.split()))
print("Tuple:", num)

print("Minimum value:", min(num))
print("Maximum value:", max(num))
print("Sum of elements:", sum(num))
print("Average value:", sum(num) / len(num))
