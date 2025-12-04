import sympy
import random


# 1. alphabet handling
# map characters to numbers:
#   " " -> 0, "A"->1, "B"->2, ..., "Z"->26
#
# these functions allow us to validate, encode, and decode text.


alphabet = [" "] + [chr(ord('A') + i) for i in range(26)]
char_to_num = {alphabet[i]: i for i in range(27)}
num_to_char = {i: alphabet[i] for i in range(27)}

def validate_plaintext(text):
    """Ensure the plaintext only contains allowed characters."""
    for c in text:
        if c not in char_to_num:
            raise ValueError(f"Invalid character in plaintext: '{c}'")

def validate_cipher(cipher_list):
    """Ensure the ciphertext is a list of non-negative integers."""
    if not all(isinstance(x, int) and x >= 0 for x in cipher_list):
        raise ValueError("Ciphertext must be a list of nonnegative integers.")


# 2. key generation
# -------------------------------------------------------------
# rabin requires primes p and q such that p ≡ q ≡ 3 (mod 4).
# this ensures that decryption is easier and produces predictable roots.
#
# keypair:
#   public key  -> n = p * q
#   private key -> (p, q)


def generate_prime(bits=16):
    """Generate a random prime p such that p % 4 == 3."""
    while True:
        p = sympy.randprime(2**(bits-1), 2**bits)
        if p % 4 == 3:
            return p

def generate_keys(bits=16):
    """
    Generate a Rabin public and private key.
    bits: size of each prime p and q (educational small values)
    """
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    return (n, (p, q))


# 3. encryption
# -------------------------------------------------------------
# convert each character to its number, then encrypt each number:
#   c = m^2 mod n
#
# this produces a list of ciphertext blocks.


def text_to_numbers(text):
    """Convert text into a list of integers according to our alphabet."""
    validate_plaintext(text)
    return [char_to_num[c] for c in text]

def numbers_to_text(nums):
    """Convert list of integers back into human-readable text."""
    return "".join(num_to_char[n] for n in nums)

def encrypt_block(m, n):
    """Encrypt a single integer m under public key n."""
    return (m * m) % n

def encrypt_text(text, n):
    """Encrypt an entire plaintext string."""
    nums = text_to_numbers(text)
    return [encrypt_block(m, n) for m in nums]


# 4. decryption
# decrypting Rabin is trickier: each ciphertext c has FOUR square roots.
# we:
#   1. compute square roots modulo p and q
#   2. use the Chinese Remainder Theorem (CRT) to combine them into 4 roots
#   3. choose the root that corresponds to a valid alphabet symbol
#
# Only one root will be in the valid range 0..26.


def crt(a1, a2, p, q):
    """
    Solve the system using the Chinese Remainder Theorem (CRT):
       x ≡ a1 (mod p)
       x ≡ a2 (mod q)
    """
    m1 = q * pow(q, -1, p)  # q * q^{-1} mod p
    m2 = p * pow(p, -1, q)  # p * p^{-1} mod q
    return (a1 * m1 + a2 * m2) % (p * q)

def decrypt_block(c, p, q):
    """Decrypt a single ciphertext block."""
    # compute square roots modulo p and q
    r_p = pow(c, (p + 1) // 4, p)
    r_q = pow(c, (q + 1) // 4, q)

    # generate all four combinations using CRT
    roots = [
        crt(r_p,        r_q, p, q),
        crt(r_p,     -r_q % q, p, q),
        crt(-r_p % p,   r_q, p, q),
        crt(-r_p % p, -r_q % q, p, q)
    ]

    # among the 4 roots, only one corresponds to a valid alphabet symbol
    for r in roots:
        if 0 <= r <= 26:
            return r

    raise ValueError("No valid plaintext root found!")

def decrypt_cipher(cipher_list, p, q):
    """Decrypt an entire list of ciphertext blocks."""
    validate_cipher(cipher_list)
    result_nums = [decrypt_block(c, p, q) for c in cipher_list]
    return numbers_to_text(result_nums)


# example usage

if __name__ == "__main__":
    # generate keys
    print("Generating keys...")
    public_key, private_key = generate_keys(bits=12)
    p, q = private_key

    print("Public key (n):", public_key)
    print("Private key (p, q):", private_key)

    plaintext = "HELLO WORLD"
    print("Plaintext:", plaintext)

    # encrypt
    cipher = encrypt_text(plaintext, public_key)
    print("Ciphertext:", cipher)

    # decrypt
    decrypted = decrypt_cipher(cipher, p, q)
    print("Decrypted:", decrypted)
