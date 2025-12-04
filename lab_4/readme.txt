Rabin Cryptosystem Project

This project implements the Rabin public key cryptosystem in Python using an alphabet of 27 characters. The alphabet contains the space character and the 26 uppercase English letters.

The Rabin cryptosystem works by taking a plaintext symbol, converting it into a number, and encrypting it using the formula c = m^2 mod n, where n is the public key. The private key consists of two primes p and q such that both p and q are congruent to 3 modulo 4. Decryption requires finding modular square roots, which produces four possible results. Only one of these values will correspond to a valid plaintext symbol.

Program flow:

Key generation:
The program generates two large primes p and q with p % 4 == 3 and q % 4 == 3. The public key is n = p * q. The private key is the pair (p, q).

Encryption:
The plaintext is validated to ensure it contains only allowed characters. Each character is converted into a number between 0 and 26. Each number m is encrypted using c = m^2 mod n. The ciphertext is a list of integers.

Decryption:
Each ciphertext value is validated. For every encrypted number c, the program computes square roots modulo p and modulo q. These are combined using the Chinese Remainder Theorem to produce four possible roots. The correct plaintext value is the one that lies between 0 and 26. After converting all decrypted numbers back to characters, the original plaintext is recovered.

Function documentation:

validate_plaintext(text)
Checks if the plaintext contains only allowed characters.

validate_cipher(cipher_list)
Checks if the ciphertext is a list of nonnegative integers.

generate_prime(bits)
Generates a random prime with the property that the prime modulo 4 equals 3.

generate_keys(bits)
Generates p and q, computes n, and returns the public and private keys.

text_to_numbers(text)
Converts plaintext characters into numbers between 0 and 26.

numbers_to_text(nums)
Converts numbers back into characters.

encrypt_block(m, n)
Encrypts a single number using m^2 mod n.

encrypt_text(text, n)
Encrypts the entire plaintext and returns ciphertext.

crt(a1, a2, p, q)
Uses the Chinese Remainder Theorem to solve for a value modulo n.

decrypt_block(c, p, q)
Computes all possible square roots and selects the correct plaintext value.

decrypt_cipher(cipher_list, p, q)
Decrypts the entire ciphertext and returns the plaintext message.

Example:
Plaintext: HELLO WORLD
Ciphertext: a list of integers produced by encryption
Decrypted text: HELLO WORLD

This implementation is intended for educational purposes and shows the full workflow of the Rabin cryptosystem in a clear and simple manner.