import random
import string

def generate_strong_password(password_length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    generated_password = ""

    for i in range(password_length):
        random_char = random.choice(all_characters)
        generated_password += random_char

    return generated_password

user_length = int(input("Enter the desired password length: "))


if user_length < 4:
    print("⚠️ Password length should be at least 4 characters.")
else:
    password = generate_strong_password(user_length)
    print("🔐 Your Generated Password:", password)
