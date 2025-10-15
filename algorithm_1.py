# this is the first verion, it's the most simple
# it's probably the most inefficient one

a = int(input("first number: ").strip())
b = int(input("second number: ").strip())

if a < b:
    while b % a !=0:
        a -= 1
    
    print("gcd is", a)
else:
    while a % b !=0:
        b -= 1
    
    print("gcd is", b)