# 🛡️ Advanced Cybersecurity Password Analyzer

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional-grade password security evaluator that utilizes prioritized breach detection and entropy-based mathematical models to classify password strength.

## ✨ Key Features

- **🗃️ RockYou Breach Detection**: Prioritizes checking the password against the 14.3M+ leaked credentials (O(1) lookup).
- **🧪 Theoretical Entropy (Brute-Force)**: Uses the formula $E = L \times \log_2(R)$ to calculate the mathematical bits of security.
- **📉 Shannon Entropy (Pattern Detection)**: Measures the randomness of the password string to penalize repeated characters and predictable patterns.
- **🔒 Secure Input**: Hidden typing using `getpass`.
- **📊 Detailed Security Report**: Provides clear breakdown of entropy scores, breach status, and length.
- **💡 Cryptographic Generator**: Suggests 18+ character high-entropy passwords for weak inputs.

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- `tqdm` library
- `rockyou.txt` (Required for breach detection)

### Installation
```powershell
pip install tqdm
```

### Usage
```powershell
python adv_pass_strength_checker.py
```

## 🛠️ Security Framework

### Classification Tiers
| Entropy (Bits) | Strength | Description |
| :--- | :--- | :--- |
| **-** | **Compromised** | Found in RockYou breach list. |
| **< 35** | **Weak** | Vulnerable to instant brute-force. |
| **36 - 59** | **Medium** | Resistant to simple attacks, vulnerable to GPU clusters. |
| **60+** | **Strong** | Cryptographically secure for standard use. |

### Entropy Metrics
1. **Theoretical Entropy**: The total search space size. This is our primary strength metric.
2. **Shannon Entropy**: A measure of "internal" randomness. If this score is too low compared to the length (e.g., `aaaaaaaaaaa`), the password is downgraded to **Weak** regardless of length.

## 🧠 Resource Usage

> [!IMPORTANT]
> **Memory Consumption**: Loading the full `rockyou.txt` database (14.3M+ passwords) into a Python set for $O(1)$ fast lookup requires approximately **400MB - 600MB of RAM**. This ensures lighting-fast analysis but may be a consideration for low-memory environments.

## 📜 License
Distribute under the **MIT License**.

---
*Developed for security portfolios and high-risk credential validation.*
