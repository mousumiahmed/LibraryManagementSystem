import sys

def password_validation(password):
    if len(password) < 8:
        print("Password must be at least 8 characters length")
        sys.exit()

    check_upper = False
    check_lower = False
    check_digit = False
    check_special = False
    for ch in password:
        if ch.isupper():
            check_upper = True
        if ch.islower():
            check_lower = True

    if not check_upper:
        print("Password must have at least one uppercase letter.")
        sys.exit()
    if not check_lower:
        print("Password must have at least one lowercase letter.")
        sys.exit()

    for ch in password:
        if ch.isdigit():
            check_digit = True

    if not check_digit:
        print("Password must have at least one digit.")
        sys.exit()

    special_ch= "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    for ch in password:
        if ch in special_ch:
            check_special = True

    if not check_special:
        print("Password must have at least one special character.")
        sys.exit()

    return True


# print(password_validation("Bvh9hbk*n"))

