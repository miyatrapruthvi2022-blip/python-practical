# Program to find common and non-common elements in two lists using membership operators

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

com = []
for i in list1:
    if i in list2:
        com.append(i)

# Step 3: Find non-common elements
ncom = []
for i in list1:
    if i not in list2:
        ncom.append(i)
for j in list2:
    if j not in list1:
        ncom.append(j)

# Step 4: Display results
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", com)
print("Non-common elements:", ncom)
