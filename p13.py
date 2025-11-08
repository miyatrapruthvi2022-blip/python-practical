#Create a sample list of 7 elements and implement the List methods mentioned: 
# append, insert, copy, extend, count, remove, pop, sort, reverse and clear. 

num = [10, 20, 30, 40, 50, 20, 60,70]
print("Original list:", num)

num.append(80)
print("After append(70):", num)

num.insert(2, 25)
print("After insert(2, 25):", num)

c = num.copy()
print("Copied list:", c)

num.extend([90])
print("After extend([90]):", num)

print("Count of 20 in list:", num.count(20))

num.remove(20)
print("After remove(20):", num)

num.pop(3)
print("After pop(3):", num)

num.sort()
print("After sort():", num)

num.reverse()
print("After reverse():", num)

num.clear()
print("After clear():", num)
