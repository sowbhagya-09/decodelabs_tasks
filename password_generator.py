import random
import string

print("=== Random Password Generator ===")

while True:
    try:
        length = int(input("Enter the password length: "))

        if length <= 0:
            print("Please enter a positive number.\n")
            continue

        characters = string.ascii_letters + string.digits

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)
        break

    except ValueError:
        print("Please enter a valid number.\n")