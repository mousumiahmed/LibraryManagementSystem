import re
import sys
import maskpass
import time
from Database import select_admin_list, show_all_users, update_password


def get_input(prompt, validation_func, max_attempts=3, mask=False):
    attempts = 0
    while attempts < max_attempts:
        if mask:
            value = maskpass.askpass(prompt)
        else:
            value = input(prompt)

        if validation_func(value):
            return value
        else:
            print(f"Invalid input. You have {max_attempts - attempts - 1} attempts left.")
        attempts += 1
    print("Max attempts reached. exited")
    sys.exit()
    # return None


def is_valid_name(name):
    if name.istitle() == True:
        return True
    else:
        print("First Character of each word must be capital !")
    return False


def is_valid_email(email):
    output = ""
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None:
        res = [item['user_email'] for item in show_all_users()]
        if res.count(email) == 0:
            output = True
        else:
            print("There is an existing account with this mail id")
            output = False
    # return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    return output


def is_valid_userType(usertype):
    return usertype.isdigit() and (int(usertype) == 1 or int(usertype) == 2)


def is_valid_password(passw):
    if len(passw) < 8:
        print("Password must be at least 8 characters length")
        return False
    if not re.search(r"[a-z]", passw):
        print("Password must have at least one lowercase letter.")
        return False
    if not re.search(r"[A-Z]", passw):
        print("Password must have at least one uppercase letter.")
        return False
    if not re.search(r"[0-9]", passw):
        print("Password must have at least one digit.")
        return False
    if not re.search(r"[\W_]", passw):
        print("Password must have at least one special character.")
        return False
    return True


def is_valid_confirmpassword(passw, confpassw):
    return passw == confpassw


def is_valid_Isbn(inp):
    # num = int(inp)
    if inp.isdigit() == True and len(inp) == 5:
        return True
    else:
        return False


def is_valid_date(date_string, date_format='%Y-%m-%d'):
    try:
        time.strptime(date_string, date_format)
        current_time = time.localtime()
        current_date_time = f"{current_time.tm_year}-{current_time.tm_mon:02d}-{current_time.tm_mday:02d} {current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"
        curr_date = time.strptime(current_date_time, "%Y-%m-%d %H:%M:%S")
        return curr_date >= time.strptime(date_string, date_format)
    except ValueError:
        return False


def is_valid_BookCount(book_count):
    if book_count.isdigit() and int(book_count) >= 0:
        return True
    else:
        return False


def check_loginchoice(inp):
    return inp.isdigit() and (int(inp) > 0 and int(inp) < 5)


def check_admin_choice(inp):
    return inp.isdigit() and (int(inp) > 0 and int(inp) < 5)


def check_user_choice(inp):
    return inp.isdigit() and (int(inp) > 0 and int(inp) < 6)


def admin_validation(inp):
    admin_list = select_admin_list()

    output = ""
    for item in admin_list:
        if item.get("id") == inp:
            if item.get("active_userid") is None:
                output = True
                break
            else:
                print("This user already have active account")
                output = False
                break
        else:
            # print("admin id wrong or doesn't exist")
            output = False
    return output


# print(admin_validation("a-30"))
def confirm_email_validation(email):
    output = ""
    if re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None:
        res = [item['user_email'] for item in show_all_users()]
        if res.count(email) == 0:
            output = False
            print("Mail id doesn't exist in our database")
        else:
            output = True
    # return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    return output


def login_password_validation(email,passwd):
    output = ""
    user = [item for item in show_all_users() if item["user_email"] == email]
    if user[0]["password"] == passwd:
        output = True
    else:
        output = False
    return output




def forgot_password(email, password):
    update_password(email, password)
    print("Your password is updated successfully !")

# user_name = get_input("Enter your name: ", is_valid_name)
# user_email = get_input("Enter your email: ", is_valid_email)
# user_type = get_input("Enter user type admin/user : ", is_valid_userType)
# password = get_input("Enter your password :", is_valid_password, mask=True)
# # confirm_password = maskpass.askpass(prompt="Confirm your Password :",mask="*")
# if password:
#     confirm_password = get_input("Confirm your password: ", lambda x: is_valid_confirmpassword(password, x), mask=True)

# # Book Add
# title = get_input("Enter the Book title(First letter of each word Capital) :", is_valid_name)
# author = get_input("Enter the Author name(First letter of each word Capital) :",is_valid_name)
# isbn = get_input("Enter the ISBN number(it must be 5 digit integer) :" , is_valid_Isbn)
# publication_date = get_input("Enter the publication date(yyyy-mm-dd) :",is_valid_date)
# book_count = get_input("Enter the book count :", is_valid_BookCount)
