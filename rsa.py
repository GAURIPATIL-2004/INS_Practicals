import math

# Step 1: User inputs for p, q, and message
p = int(input("Enter a prime value for p: "))
q = int(input("Enter a prime value for q: "))
msg = int(input("Enter the message (integer): "))

# Step 2: Calculate n
n = p * q
print("n =", n)

# Step 3: Calculate phi (Euler's Totient)
phi = (p - 1) * (q - 1)

# Step 4: Find public exponent e (smallest coprime to phi)
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
print("e =", e)

# Step 5: Calculate private key d
k = 2  # A constant multiplier, can be adjusted
d = int(((k * phi) + 1) / e)
print("d =", d)
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

# Encryption
C = pow(msg, e, n)  # Encrypt the message
print(f'Encrypted message: {C}')

# Decryption
M = pow(C, d, n)  # Decrypt the message
print(f'Decrypted message: {M}')