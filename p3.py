#Write a program to create a byte type array, read, modify,and display the elements of the array
data=bytearray([5,10,15,20,25])

print("Original array")
for value in data:
    print(value,end =" ")

print("\nModify Array")
for i in range(len(data)):
    data[i]=data[i]+5

for value in data:
    print(value,end = " ")

