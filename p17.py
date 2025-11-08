# Write a program to convert the elements of two lists into key value pairs of 
# a dictionary. 
keys = ["name", "age", "city"]
values = ["Pruthvi", 21, "Ahmedabad"]

my = dict(zip(keys, values))

print("Dictionary created from two lists:")
print(my)
