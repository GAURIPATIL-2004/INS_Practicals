def encode(key, plaintext):
    # Step 1: Create columns based on key length
    cols = [''] * len(key)
    for i, c in enumerate(plaintext):
        cols[i % len(key)] += c
    
    # Step 2: Sort columns based on the order of the key
    ordered_cols = [cols[i] for i in sorted(range(len(key)), key=lambda k: key[k])]
    
    # Step 3: Combine the columns to get the encoded message
    return ''.join(ordered_cols)

key = input("Enter the key: ")
plain = input("Enter the message: ")
print("Encoded message:", encode(key, plain))