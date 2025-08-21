import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Must be at least 4 characters."
    
    # All possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Get user input
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print(f"\n🔐 Generated Password: {password}")
except ValueError:
    print("❌ Please enter a valid number!")
