def encrypt_message(message, key):
    message = message.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = len(message) // num_cols + (len(message) % num_cols != 0)
    grid = ['' for _ in range(num_cols)]
    
    for idx, char in enumerate(message):
        col = idx % num_cols
        grid[col] += char

    sorted_key_indices = sorted(range(len(key)), key=lambda x: key[x])
    encrypted_message = ''.join(grid[i] for i in sorted_key_indices)
    
    return encrypted_message

message = input("Enter message: ")
key = input("What is your key: ")

encrypted_message = encrypt_message(message, key)
print("Encrypted message:", encrypted_message)