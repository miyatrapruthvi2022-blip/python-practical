def student(name, age, course="BCA", *subjects):
    print("Name:", name)                   # Positional or Keyword
    print("Age:", age)                     # Positional or Keyword
    print("Course:", course)               # Default argument
    print("Subjects:", subjects)           # Variable length arguments
    print()  # blank line for clarity

# 1️⃣ Positional Arguments
student("Pruthvi", 20, "BCA")

# 2️⃣ Keyword Arguments
student(name="Ravi", age=21, course="BBA", subjects="Maths")

# 3️⃣ Default Argument (no course passed → uses default "BCA")
student("Karan", 19)

# 4️⃣ Variable Length Arguments (multiple subjects)
student("Rahul", 22, "MCA", "AI", "ML", "DBMS")
