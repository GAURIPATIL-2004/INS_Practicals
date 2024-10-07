def vernam(text, key): 
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))

# Input
text = input("Enter message: ").upper().replace(" ", "")
key = input("Enter key: ").upper()

# Encryption
cipher_text = vernam(text, key)
print("Encrypted Message:", cipher_text)

# Decryption (same function with the same key)
decrypted_text = vernam(cipher_text, key)
print("Decrypted Message:", decrypted_text)