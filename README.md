# cyberguard-security-system

## How to run

```bash
python3 cyberguard.py
```# CyberGuard Security System

CyberGuard is a simple Python program that acts as a security monitoring tool for a junior cybersecurity analyst. It collects account information, checks login activity, finds possible threats and prints a security report.

## What CyberGuard Does

The program asks for details about a user account and then analyses them. It checks the number of failed login attempts, whether the account is active, and how strong the password is. At the end it prints a report that changes depending on the information entered.

## Features

- **Welcome screen** shown when the program starts
- **User information collection** for username, email, password, age, IP address, failed login attempts and account status
- **Threat detection**
  - 0 failed attempts: no failed login attempts detected
  - 1 to 4 failed attempts: low security alert
  - 5 or more failed attempts: critical warning, possible brute-force attack
  - Inactive account: access is disabled
  - Active account with fewer than 5 attempts: no critical login threat
- **Password strength checker** based on length
  - Fewer than 8 characters: weak
  - 8 to 11 characters: moderate
  - 12 or more characters: strong
- **Security report** with a threat level (LOW, MEDIUM or HIGH) and a recommendation. The actual password is never shown.

## Python Concepts Used

- Variables
- Strings, integers, floats and Booleans
- `input()` and `print()`
- `type()`
- Type conversion with `str()`, `int()` and `float()`
- Assignment and comparison operators
- `if`, `elif` and `else`

## How to Run

1. Install Python 3 from python.org.
2. Download `cyberguard.py` from this repository.
3. Open a terminal in the folder that contains the file.
4. Run:


