import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Use at least 4 characters for strength.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Enter a valid number.")

if __name__ == "__main__":
    main()