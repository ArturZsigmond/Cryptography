# this is the first verion, it's the most simple
# it's probably the most inefficient one

a = int(input("first number: ").strip())
b = int(input("second number: ").strip())

def gcd_basic(a, b):
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    if a == b: return a
    if a > b and a % b == 0: return b
    if b > a and b % a == 0: return a

    d = min(a, b)
    while d > 1 and ((a % d != 0) or (b % d != 0)):
        d -= 1
    return d


print("gcd is", gcd_basic(a, b))