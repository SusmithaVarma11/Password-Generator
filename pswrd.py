import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number!")
        