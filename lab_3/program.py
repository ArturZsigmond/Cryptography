import math
from math import gcd

def is_perfect_square(x):
    """
    Returns True if x is a perfect square, False otherwise.
    A fast integer-based check using math.isqrt().
    """
    if x < 0:
        return False
    y = math.isqrt(x)     # integer square root
    return y * y == x


def generalized_fermat(n):
    """
    Applies the Generalized Fermat’s factorization algorithm.
    It tries k = 1, 2, 3, ... until it finds a non-trivial factor of n.

    n: integer to be factored.
    Returns: (factor1, factor2)
    """
    if n % 2 == 0:
        # Quick check for even numbers
        return 2, n // 2

    k = 1  # Start with k = 1

    while True:
        # compute N = n * k
        N = n * k

        # compute a = ceil(sqrt(N))
        a = math.isqrt(N)
        if a * a < N:
            a += 1

        # compute b^2 = a^2 - N
        b2 = a * a - N

        # Check if b2 is a perfect square
        if is_perfect_square(b2):
            b = math.isqrt(b2)

            # Compute the possible factors using the difference of squares:
            # n = (a - b)(a + b) / k
            # But we must use gcd because (a ± b) might contain extra k factors.
            d1 = gcd(a - b, n)
            d2 = gcd(a + b, n)

            # Check if these are non-trivial factors
            if d1 not in (1, n):
                return d1, n // d1
            if d2 not in (1, n):
                return d2, n // d2

        # If no factor found, increase k and try again
        k += 1


def main():
    """
    Main function allowing the user to input a number and see its factors.
    """
    print("Generalized Fermat Factorization Algorithm")
    n = int(input("Enter a number to factor: "))

    if n <= 1:
        print("Please enter an integer greater than 1.")
        return

    f1, f2 = generalized_fermat(n)

    print("\nFactors found:")
    print(f"{n} = {f1} × {f2}")


if __name__ == "__main__":
    main()
