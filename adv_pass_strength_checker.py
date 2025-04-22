import re
import math
import random
import string
from tqdm import tqdm
import time

# Common passwords (small list for demo; extend with a file in production)
COMMON_PASSWORDS = {'password', '123456', 'qwerty', 'admin', 'letmein'}

def calculate_entropy(password):
    """Calculate Shannon entropy of the password (in bits)."""
    if not password:
        return 0
    char_count = {}
    for char in password:
        char_count[char] = char_count.get(char, 0) + 1
    entropy = 0
    length = len(password)
    for count in char_count.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
    return entropy

def generate_strong_password(length=16):
    """Generate a strong random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_password_strength(password):
    """Evaluate password strength with advanced criteria."""
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    else:
        feedback.append("Password is too short. Use at least 12 characters for optimal security.")

    # Check character variety
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters to increase complexity.")
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters to increase complexity.")
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers to increase complexity.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        feedback.append("Add special characters (e.g., !, @, #) for better strength.")

    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("Avoid repeating the same character more than twice in a row.")

    # Check for common patterns (e.g., 'abc', '123')
    if re.search(r'(abc|123|qwe)', password, re.IGNORECASE):
        score -= 1
        feedback.append("Avoid common patterns like 'abc' or '123'.")

    # Check against common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a common password. Choose a unique one.")

    # Check entropy
    entropy = calculate_entropy(password)
    if entropy >= 4:
        score += 2
    elif entropy >= 3:
        score += 1
    else:
        feedback.append("Password lacks randomness. Use a more varied character set.")

    # Determine strength
    if score >= 10 or (score >= 8 and entropy >= 4):
        strength = "Strong"
    elif score >= 6:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback, entropy

def main():
    print("Advanced Password Strength Checker")
    print("Note: Password input will be visible in some environments (e.g., VS Code).")
    print("For hidden input, run this script in a standard terminal (e.g., Command Prompt).")
    password = input("Enter your password: ")

    if not password:
        print("Password cannot be empty!")
        return

    # Simulate analysis with progress bar
    print("Analyzing password strength...")
    for _ in tqdm(range(100), desc="Processing", ncols=80):
        time.sleep(0.01)  # Simulate processing time

    strength, feedback, entropy = check_password_strength(password)

    # Display results
    print(f"\nPassword Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits (higher is better)")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Your password is strong and meets all advanced criteria!")

    # Suggest a strong password if weak
    if strength == "Weak":
        suggested_password = generate_strong_password()
        print(f"\nSuggested strong password: {suggested_password}")

if __name__ == "__main__":
    main()