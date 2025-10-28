from math import gcd
from functools import reduce

def extended_gcd(a, b):
    """Extended Euclidean Algorithm: returns (g, x, y) such that a*x + b*y = g = gcd(a, b)."""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def mod_inverse(a, m):
    """Find modular inverse of a mod m (a*x ≡ 1 mod m)."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}.")
    return x % m

def chinese_remainder_theorem(remainders, moduli):
    """Solve x ≡ a_i (mod n_i) for all i (Chinese Remainder Theorem)."""
    if len(remainders) != len(moduli):
        raise ValueError("Remainders and moduli lists must have the same length.")
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli are not pairwise coprime.")
    M = reduce(lambda a, b: a * b, moduli, 1)
    total = 0
    for ai, ni in zip(remainders, moduli):
        Mi = M // ni
        inv = mod_inverse(Mi, ni)
        total += ai * Mi * inv
    return total % M, M

# ---------------------------
# Hardcoded example system:
# Solve:
# x ≡ 2 (mod 3)
# x ≡ 3 (mod 5)
# x ≡ 2 (mod 7)
# ---------------------------
remainders = [2, 3, 2]
moduli = [3, 5, 7]

solution, modulo = chinese_remainder_theorem(remainders, moduli)

print("System of congruences:")
for a, n in zip(remainders, moduli):
    print(f"x ≡ {a} (mod {n})")

print(f"\nSolution: x ≡ {solution} (mod {modulo})")
