import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1

    if score <= 2:
        return "Weak Password"

    elif score <= 4:
        return "Moderate Password"

    else:
        return "Strong Password"


password = input("Enter Password: ")

result = check_password_strength(password)

print("\nPassword Analysis")
print("------------------")
print("Strength:", result)