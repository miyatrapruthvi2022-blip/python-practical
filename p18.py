def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

print("Prime numbers from 1 to", num, "are:")
for i in range(1, num + 1):
    if isprime(i):
        print(i)

if isprime(num):
    print(num, "is a Prime number")
else:
    print(num, "is Not a Prime number")