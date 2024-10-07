import random

# This is your main code block.
message = input("Enter message: ")  # Prompt user for a message
key = input("What is your key: ")    # Prompt user for a key

random.seed(str(key))  # Seed the random generator with the key

# Shuffle the characters of the message
r = ''.join(random.sample(message, len(message)))

# Print the shuffled message as one word
print("Shuffled message:", r)