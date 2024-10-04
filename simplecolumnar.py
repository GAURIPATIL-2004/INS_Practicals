def split_len(seq, length):
    # Split the plaintext into chunks of length equal to the length of the key
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
    # Map the key digits to their order in the key
    order = {int(val): num for num, val in enumerate(key)}
    
    ciphertext = ''
    
    # Sort the key in ascending order and build the ciphertext
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                # Handle cases where a part is shorter than the key length
                continue
    
    return ciphertext

# Input handling
key = input("Enter the number sequence as key: ")  # Example: '3142'
plain = input("Enter the message: ")

# Output the encoded message
print("Encoded message:", encode(key, plain))