Advanced Password Strength Checker

Overview

This project provides a Python script (advanced_password_strength_checker.py) to evaluate the strength of passwords using advanced criteria. It assesses length, character variety, repeated characters, common patterns, common passwords, and Shannon entropy, assigning a strength score (Weak, Medium, Strong). The script offers actionable feedback, a visual progress bar, and generates a strong password if the input is weak. It's ideal for validating passwords in security-focused applications, such as file encryption tools.

Features

Comprehensive Evaluation:

Length: ≥12 chars (3 points), 8–11 (2 points), 6–7 (1 point).



Character variety: Uppercase, lowercase, digits (+1 each), special characters (+2).



Repeated characters and common patterns (e.g., "abc", "123"): -1 point each.



Common passwords: Resets score to 0 if matched.



Shannon entropy: Measures randomness (≥4 bits: +2, ≥3 bits: +1).



Strength Scoring:




Strong: Score ≥ 10 or (score ≥ 8 and entropy ≥ 4).



Medium: Score ≥ 6.



Weak: Score < 6.



Feedback: Provides suggestions to improve weak passwords.



Progress Bar: Visual analysis feedback using tqdm.



Password Generation: Suggests a 16-character random strong password for weak inputs.



Compatibility: Uses input() for environments like VS Code, with a note about visible input.

Requirements
Python 3.6 or higher
tqdm library for the progress bar

Installation
Clone or Download the Project:
Clone the repository or download the advanced_password_strength_checker.py file.
Install Dependencies:
pip install tqdm
No other dependencies are required (uses standard Python libraries).

Usage
Run the Script:
python advanced_password_strength_checker.py
Enter a Password:
You'll be prompted to enter a password.
Note: In some environments (e.g., VS Code integrated terminal), the password will be visible. For hidden input, run in a standard terminal (e.g., Command Prompt, Linux terminal).
View Results:
The script analyzes the password and outputs:
Strength (Weak, Medium, Strong)
Entropy (in bits)
Suggestions (if applicable)



A suggested strong password (if weak)

Example

$ python advanced_password_strength_checker.py
Advanced Password Strength Checker
Note: Password input will be visible in some environments (e.g., VS Code).
For hidden input, run this script in a standard terminal (e.g., Command Prompt).
Enter your password: pass123
Analyzing password strength...
Processing: [██████████] 100%
Password Strength: Weak
Entropy: 2.58 bits (higher is better)
Suggestions to improve your password:
- Password is too short. Use at least 12 characters for optimal security.
- Add uppercase letters to increase complexity.
- Add special characters (e.g., !, @, #) for better strength.
- Avoid common patterns like 'abc' or '123'.
- Password lacks randomness. Use a more varied character set.
Suggested strong password: kX9#mP2$vNqL&jR5

Notes
Security:
The script uses input() for compatibility with IDEs like VS Code, but this makes the password visible during entry. For hidden input, run in a standard terminal.
The common password list is small for demo purposes. In production, use a larger database.

Extensibility:
Add a file-based common password list for better coverage.
Integrate with a GUI (e.g., Tkinter) to mask password input.
Pair with encryption tools to validate passwords for encryption keys.

Limitations:
Entropy is a guide, not a perfect security measure.
Does not check for keyboard patterns (e.g., zxcvbn); this can be added.

VS Code Users:
If you prefer hidden input, run the script in an external terminal or revert to using getpass.getpass() (may require terminal settings adjustments).

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions, bug reports, or feature requests.
