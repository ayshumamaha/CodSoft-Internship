import random
import string

print("----- Password Generator -----")

try:
    length = int(input("Enter desired password length: "))

    if length <= 0:
        print("Please enter a valid positive number.")
    else:
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        all_characters = letters + digits + symbols

        password = ""
        for _ in range(length):
            password += random.choice(all_characters)

        print("Generated Password:", password)

except ValueError:
    print("Please enter numbers only.")
    
