
def email_verification(str):
    email = str.strip().lower()
    if not "@" in email:
        print("Invalid email")

    elif not email[-4:] in ".com.org.edu.gov.net":
        print("Invalid email")

