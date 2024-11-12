import random
import string

def generate_password(length):
    # Define the characters to choose from
    character_pool = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choices(character_pool, k=length))

    return password

# Get user input for password length
length = int(input("Enter the desired length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Generated password:", password)
print("\n")