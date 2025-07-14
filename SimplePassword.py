import string

# Step 1: Get password from user
password = input("Enter your password: ")

# Step 2: Define all required conditions
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)
is_long_enough = len(password) >= 8

# Step 3: Check each condition and report
if is_long_enough and has_upper and has_lower and has_digit and has_special:
    print("Password strength is GOOD ✅")
else:
    print("Password is NOT strong ❌. Please follow the password format:")
    print("→ Minimum 8 characters")
    print("→ At least 1 uppercase letter")
    print("→ At least 1 lowercase letter")
    print("→ At least 1 number")
    print("→ At least 1 special character (@, #, $, %, etc.)")

    # Optional: show which specific condition is missing
    print("\nMissing conditions:")
    if not is_long_enough:
        print("✖ Minimum 8 characters")
    if not has_upper:
        print("✖ At least 1 uppercase letter")
    if not has_lower:
        print("✖ At least 1 lowercase letter")
    if not has_digit:
        print("✖ At least 1 number")
    if not has_special:
        print("✖ At least 1 special character")