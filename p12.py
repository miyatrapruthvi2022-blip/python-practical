#Write a program to create a list using range functions and 
#perform append, update and delete elements operations in it. 

num = list(range(1, 6))   # This will create [1, 2, 3, 4, 5]
print("Original list:", num)

num.append(6)
print("After appending 6:", num)

num[2] = 30
print("After updating 3rd element:", num)

del num[3]
print("After deleting 4th element:", num)
