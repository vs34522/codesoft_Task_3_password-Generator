import random
import string

# Function to generate password
def generate_password(length):
    if length < 4:
        return "Password length must be at least 4."

    # All characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(all_characters)

    return password

# Ask the user for length
user_input = input("Enter password length: ")

# Check if input is a number
if user_input.isdigit():
    length = int(user_input)
    password = generate_password(length)
    print("Generated Password:", password)
else:
    print("Please enter a valid number.")
