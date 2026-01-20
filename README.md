# 🛡️ Advanced Password Strength Checker

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust and feature-rich Python utility designed to evaluate password security using multi-layered analysis. It goes beyond simple length checks by incorporating Shannon entropy, pattern recognition, and heuristics for common security pitfalls.

## ✨ Key Features

- **🔍 Multi-Layered Analysis**: Evaluates length, character variety (uppercase, lowercase, digits, symbols), and Shannon entropy.
- **🚫 Pattern Recognition**: Detects repeated characters and sequential patterns (e.g., `abc`, `123`).
- **🔄 Reversed Pattern Detection**: Identifies descending sequences such as `321`, `cba`, or `zyx`.
- **⚠️ Predictable Placement Penalty**: Heuristic checks for common habits, like starting with an uppercase letter and ending with a digit (e.g., `Password123`).
- **🔒 Secure Input**: Uses `getpass` to ensure passwords are hidden while typing in the terminal.
- **📊 Visual Progress**: Integrated `tqdm` progress bar for a modern CLI experience.
- **💡 Smart Suggestions**: Provides actionable feedback to improve weak passwords.
- **🎲 Password Generator**: Automatically suggests a cryptographically strong 16-character password if the input is weak.

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- `tqdm` library

### Installation
1. **Clone the repository:**
   ```powershell
   git clone https://github.com/nahom1011/star-python.git
   cd star-python
   ```
2. **Install dependencies:**
   ```powershell
   pip install tqdm
   ```

### Usage
Run the script directly from your terminal:
```powershell
python adv_pass_strength_checker.py
```

## 🛠️ Technical Details

### Scoring System
| Criteria | Logic | Score Adjustment |
| :--- | :--- | :--- |
| **Length** | >= 12 chars | +3 |
| **Length** | 8 - 11 chars | +2 |
| **Variety** | Uppercase, Lowercase, Digits | +1 each |
| **Variety** | Special Characters | +2 |
| **Entropy** | >= 4 bits | +2 |
| **Entropy** | >= 3 bits | +1 |
| **Bad Habits** | Repeated chars / Common Patterns | -1 |
| **Bad Habits** | Reversed Patterns / Predictable Placement | -1 |

### Entropy Analysis
The tool calculates **Shannon Entropy** to measure the randomness of the password. Higher entropy values indicate a password that is harder to crack via brute-force or dictionary attacks.

## 📝 Example Output

```text
Advanced Password Strength Checker
Enter your password: 
Analyzing password strength...
Processing: 100%|█████████████████████████████| 100/100 [00:01<00:00]

Password Strength: Strong
Entropy: 5.68 bits (higher is better)
Your password is strong and meets all advanced criteria!
```

## 📜 License
Distribute under the **MIT License**. See `LICENSE` for more information.

---
*Developed for the security-conscious developer.*
