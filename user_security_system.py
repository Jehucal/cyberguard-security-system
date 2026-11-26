# CyberGuard - security monitoring program

# Welcome screen
print("========================================")
print("           CYBERGUARD v1.0")
print("     PERSONAL SECURITY MONITORING SYSTEM")
print("========================================")
print("")
print("Welcome, Security Analyst!")
print("")
print("Your mission is to monitor account")
print("information and identify potential threats.")
print("")
print("Starting security assessment...")
print("")

# Get the user information
username = input("Enter username: ")
email = input("Enter email address: ")
password = input("Enter password: ")
age = int(input("Enter age: "))
ip_address = input("Enter IP address: ")
failed_attempts = int(input("Enter failed login attempts: "))
status = input("Is the account Active or Inactive? ")

# Turn the status into True or False
if status == "Active" or status == "active":
    account_active = True
else:
    account_active = False

# Check the data types
print("")
print("Checking data types...")
print(type(username))
print(type(age))
print(type(failed_attempts))
print(type(account_active))

# Age as a float
age_float = float(age)
print(age_float)
print(type(age_float))

# Password strength (using length)
password_length = len(password)

if password_length < 8:
    password_result = "WEAK"
elif password_length < 12:
    password_result = "MODERATE"
else:
    password_result = "STRONG"

# Account status text
if account_active == True:
    status_text = "ACTIVE"
else:
    status_text = "INACTIVE"

# Check failed login attempts
if failed_attempts == 0:
    message1 = "[OK] No failed login attempts detected."
    message2 = ""
    threat = "LOW"
elif failed_attempts >= 1 and failed_attempts <= 4:
    message1 = "[LOW ALERT] Some failed login attempts."
    message2 = ""
    threat = "LOW"
else:
    message1 = "[CRITICAL] Multiple failed login attempts!"
    message2 = "[WARNING] Possible brute-force attack detected."
    threat = "HIGH"

# Check if the account is active
if account_active == False:
    message3 = "[NOTICE] Account is inactive. Access is disabled."
elif failed_attempts < 5:
    message3 = "[OK] No critical login threat detected."
else:
    message3 = ""

# Recommendation
if threat == "HIGH":
    recommendation = "Investigate the login activity and secure the account immediately."
elif password_result == "WEAK":
    recommendation = "Ask the user to use a stronger password."
else:
    recommendation = "No action needed. Keep monitoring the account."

# Print the report (the password is not shown)
print("")
print("========================================")
print("          CYBERGUARD SECURITY REPORT")
print("========================================")
print("")
print("USER INFORMATION")
print("----------------------------------------")
print("Username: " + username)
print("Email: " + email)
print("Age: " + str(age))
print("IP Address: " + ip_address)
print("Account Status: " + status_text)
print("")
print("SECURITY ANALYSIS")
print("----------------------------------------")
print("Password Assessment: " + password_result)
print("Failed Login Attempts: " + str(failed_attempts))
print("")
print("THREAT DETECTION")
print("----------------------------------------")
print(message1)
if message2 != "":
    print(message2)
if message3 != "":
    print(message3)
print("")
print("FINAL SECURITY STATUS")
print("----------------------------------------")
print("THREAT LEVEL: " + threat)
print("")
print("RECOMMENDATION:")
print(recommendation)
print("")
print("========================================")
print("          END OF SECURITY REPORT")
print("========================================")