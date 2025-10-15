def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
# Each recursive call reduces the size of the numbers significantly using 
# the modulo operation (a % b), which shrinks the input faster than subtraction.
a = int(input("first number: ").strip())
b = int(input("second number: ").strip())

print("gcd is", gcd(a, b))