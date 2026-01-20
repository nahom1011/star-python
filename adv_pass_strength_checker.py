import re
import math
import random
import string
from tqdm import tqdm
import time
import getpass
import os

# Global set for fast O(1) lookup of common passwords
COMMON_PASSWORDS = set()

def load_common_passwords(file_path="rockyou.txt"):
    """
    Efficiently loads the RockYou database into a set.
    Uses 'utf-8' with 'replace' and 'latin-1' fallback for robustness.
    """
    global COMMON_PASSWORDS
    if not os.path.exists(file_path):
        print(f"⚠️ Warning: {file_path} not found. Breach detection disabled.")
        return False
    
    print(f"🔍 Initializing security database ({file_path})...")
    try:
        # Many password lists have non-UTF8 characters; latin-1 is safer for raw bytes
        with open(file_path, "r", encoding="latin-1", errors="replace") as f:
            for line in tqdm(f, desc="Loading Database", unit="lines", ncols=80):
                COMMON_PASSWORDS.add(line.strip())
        return True
    except Exception as e:
        print(f"❌ Error loading database: {e}")
        return False

def calculate_shannon_entropy(password):
    """
    Calculates Shannon Entropy (H).
    Measures the randomness/unpredictability based on character frequency.
    Lower H indicates high repetition (e.g., 'aaaaaa').
    """
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

def calculate_theoretical_entropy(password):
    """
    Calculates Theoretical Brute-Force Entropy (E).
    Formula: E = L * log2(R)
    L = Password Length
    R = Character Set Size (Pool)
    """
    if not password:
        return 0, 0, 0
    
    length = len(password)
    pool_size = 0
    
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    if has_lower: pool_size += 26
    if has_upper: pool_size += 26
    if has_digit: pool_size += 10
    if has_symbol: pool_size += 32 # standard string.punctuation size is ~32
    
    # Handle characters not in the standard set (other ASCII/Unicode)
    if pool_size == 0:
        pool_size = 95 # Standard printable ASCII range
        
    theoretical_bits = length * math.log2(pool_size)
    return theoretical_bits, length, pool_size

def generate_strong_password(length=18):
    """Generates a high-entropy cryptographically strong password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.getcurrent().choice(chars) if hasattr(random, 'getcurrent') else random.SystemRandom().choice(chars) for _ in range(length))

def check_password_strength(password):
    """
    Main evaluation engine. 
    Prioritizes Breach Detection -> Theoretical Entropy -> Shannon Refinement.
    """
    # 1. Check RockYou Breach Database (Highest Priority)
    is_compromised = password in COMMON_PASSWORDS
    
    # 2. Entropy Calculations
    shannon_h = calculate_shannon_entropy(password)
    brute_force_bits, length, pool = calculate_theoretical_entropy(password)
    
    # 3. Strength Classification
    if is_compromised:
        strength = "Compromised"
        color_code = "RED"
    elif brute_force_bits < 35:
        strength = "Weak"
        color_code = "YELLOW"
    elif brute_force_bits < 60:
        strength = "Medium"
        color_code = "BLUE"
    else:
        strength = "Strong"
        color_code = "GREEN"
        
    # 4. Pattern Refinement (Shannon Entropy Penalty)
    # If Shannon entropy is very low relative to length, user is repeating characters
    # Ideal Shannon for unique chars is log2(len)
    if length > 0:
        max_possible_h = math.log2(length) if length > 1 else 1
        h_ratio = shannon_h / max_possible_h if max_possible_h > 0 else 0
        if h_ratio < 0.5 and strength != "Compromised":
            strength = "Weak (Highly Patterned)"

    return {
        "strength": strength,
        "is_compromised": is_compromised,
        "shannon_entropy": shannon_h,
        "theoretical_entropy": brute_force_bits,
        "length": length,
        "pool_size": pool
    }

def main():
    # Performance: Load once at startup
    db_loaded = load_common_passwords()

    print("\n" + "="*50)
    print("🛡️  ADVANCED CYBERSECURITY PASSWORD ANALYZER")
    print("="*50)

    try:
        password = getpass.getpass("🔑 Enter Password to Analyze: ")
    except KeyboardInterrupt:
        print("\nExiting...")
        return

    if not password:
        print("❌ Error: Password cannot be empty.")
        return

    print("\n⚙️  Performing multi-layered security analysis...")
    # Add a slight delay for better UX (simulating complex check)
    for _ in tqdm(range(100), desc="Analyzing", ncols=80, leave=False):
        time.sleep(0.005)

    results = check_password_strength(password)

    # --- REPORT DISPLAY ---
    print("\n" + "-"*30)
    print(f"📊 SECURITY REPORT")
    print("-"*30)
    
    if results["is_compromised"]:
        print(f"⚠️  BREACH STATUS: FOUND IN ROCKYOU DATABASE!")
        print(f"   [CAUTION] This password has been leaked and is functionally useless.")
    else:
        print(f"✅ BREACH STATUS: NOT FOUND IN KNOWN LEAKS")

    print(f"\n📏 Length: {results['length']} characters")
    print(f"🎲 Character Pool: {results['pool_size']} (possible unique chars)")
    print(f"🧪 Theoretical Entropy: {results['theoretical_entropy']:.2f} bits")
    print(f"📉 Shannon Entropy: {results['shannon_entropy']:.2f} (randomness score)")
    
    print("-"*30)
    print(f"🏆 FINAL RATING: {results['strength'].upper()}")
    print("-"*30)

    if results["strength"] in ["Compromised", "Weak", "Weak (Highly Patterned)"]:
        print("\n💡 RECOMMENDATION: Upgrade your password immediately.")
        print(f"   Suggested Secure Password: {generate_strong_password()}")
    elif results["strength"] == "Medium":
        print("\n💡 RECOMMENDATION: Consider adding more variety or symbols.")
    else:
        print("\n🌟 EXCELLENT: This password meets professional security standards.")

    print("="*50 + "\n")

if __name__ == "__main__":
    main()