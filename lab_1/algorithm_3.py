def gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case
    if a == b:
        return a

    # a is greater
    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)

    # b is greater
    if b % a == 0:
        return a
    return gcd(a, b - a)

a = int(input("first number: ").strip())
b = int(input("second number: ").strip())
print(gcd(a, b))