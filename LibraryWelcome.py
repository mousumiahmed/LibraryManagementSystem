import sys
from BookRemove import Book_Remove
from ShowAllBooks import show_all_book_details
import maskpass
from BookUpdate import book_Checkout, Book_Return
from SearchBook import Search_Book
from UserInputVerifications import (get_input, is_valid_name, is_valid_email,
                                    is_valid_userType, is_valid_password, is_valid_confirmpassword, is_valid_date,
                                    is_valid_Isbn, is_valid_BookCount, check_loginchoice, check_admin_choice,
                                    check_user_choice,
                                    admin_validation, forgot_password, confirm_email_validation,
                                    login_password_validation)

from Database import insert_user, insert_books, show_all_books, show_all_users, update_active_admin

user_list = show_all_users()
book_list = show_all_books()


# print(user_list)


def welcome(user_choice):
    if int(user_choice) == 1:
        print("welcome to login page")

        def user_login(email, password):
            res_str = ""
            for it in user_list:
                if it.get("user_email") == email and it.get("password") == password:
                    if it.get("user_type") == 1:
                        res_str = 1
                        break
                    elif it.get("user_type") == 2:
                        res_str = 2
                        break
                else:
                    res_str = "incorrect"

            if res_str == 1:
                print("You are now admin page")
                while True:
                    operation = get_input("choose next operation 1.add/2.remove/3.show/4.exit :", check_admin_choice)
                    if int(operation) == 1:
                        def Book_Registration(title, author, isbn, publication_date, book_count):
                            book_details = {}
                            book_details["title"] = title
                            book_details["author"] = author
                            book_details["isbn"] = isbn
                            book_details["publication_date"] = publication_date
                            book_details["book_count"] = book_count
                            # return book_details

                            for ite in book_list:
                                if ite['title'] == title:
                                    return "Book is already exist"
                                else:
                                    book_list.append(book_details)
                                    insert_books(book_details, email)
                                    return "Book is registered successfully"

                        while True:

                            title = get_input("Enter the Book title(First letter of each word Capital) :",
                                              is_valid_name)
                            author = get_input("Enter the Author name(First letter of each word Capital) :",
                                               is_valid_name)
                            isbn = get_input("Enter the ISBN number(it must be 5 digit integer) :", is_valid_Isbn)
                            publication_date = get_input("Enter the publication date(yyyy-mm-dd) :", is_valid_date)
                            book_count = get_input("Enter the book count :", is_valid_BookCount)

                            print(Book_Registration(title, author, isbn, publication_date, book_count))

                            user_input = int(input("Do you want to add book again? (1.Yes/2.No): "))
                            if user_input != 1:
                                break

                    if int(operation) == 2:
                        book_title = input("Enter the book title :")
                        Book_Remove(book_list, book_title)
                    elif int(operation) == 3:
                        show_all_book_details(book_list)
                    elif int(operation) == 4:
                        print("we are exiting from this window")
                        break
                        # sys.exit()
            elif res_str == 2:
                print("You are welcome to library user page !")
                while True:
                    user_inp = get_input(
                        "Pls Input what you looking for- 1.showallbook/2.searchbyname/3.checkout/4.return/5.exit : ",
                        check_user_choice)

                    if int(user_inp) == 1:
                        show_all_book_details(book_list)
                    elif int(user_inp) == 2:
                        # print("searching book by name")
                        book_name = get_input("Enter the book name you want to Search :", is_valid_name)
                        Search_Book(book_list, book_name)
                    elif int(user_inp) == 3:
                        book_name = input("Enter the book name you want to checkout :")
                        book_Checkout(book_name, email)
                    elif int(user_inp) == 4:
                        book_name = input("Enter the book name you want to return :")
                        Book_Return(book_name, email)
                    elif int(user_inp) == 5:
                        # sys.exit()
                        break

            elif res_str == "incorrect":
                print("Wrong credential entered ! ")

        email = get_input("Enter your email :", confirm_email_validation)
        password = ""
        if email:
            password = get_input("Enter your password: ", lambda x: login_password_validation(email, x),
                                 mask=True)

        user_login(email, password)
    elif int(user_choice) == 2:
        print("welcome to user registration page")

        def User_Registration(user_name, user_email, user_type, password, confirm_password, adminid):
            user_details = {}

            user_details["user_name"] = user_name
            user_details["user_email"] = user_email
            user_details["user_type"] = int(user_type)
            user_details["password"] = password
            user_details["confirm_password"] = confirm_password
            for ite in user_list:
                if ite['user_email'] == user_email:
                    return "User email is already exist"
                else:
                    user_list.append(user_details)
                    insert_user(user_details)
                    if adminid != "":
                        update_active_admin(user_email, adminid)
                    return "You have successfully registered"

            # else:
            #     return "confirm password is not matching"

        user_name = get_input("Enter your name(First letter of each word Capital): ", is_valid_name)
        user_email = get_input("Enter your email: ", is_valid_email)
        user_type = get_input("Enter user type 1.admin/2.user : ", is_valid_userType)
        admin_id = ""
        if int(user_type) == 1:
            admin_id = get_input("Enter admin id :", admin_validation)
        password = get_input("Enter your password :", is_valid_password, mask=True)
        # confirm_password = maskpass.askpass(prompt="Confirm your Password :", mask="*")
        confirm_password = ""
        if password:
            confirm_password = get_input("Confirm your password: ", lambda x: is_valid_confirmpassword(password, x),
                                         mask=True)
        # else:
        #     confirm_password = None
        print(User_Registration(user_name, user_email, user_type, password, confirm_password, admin_id))
    elif int(user_choice) == 3:
        confirm_email = get_input("Enter your email: ", confirm_email_validation)

        new_password = get_input("Enter your new password :", is_valid_password, mask=True)
        confirm_newpassword = ""
        if new_password:
            confirm_newpassword = get_input("Confirm your password: ",
                                            lambda x: is_valid_confirmpassword(new_password, x),
                                            mask=True)
        forgot_password(confirm_email, confirm_newpassword)

    elif int(user_choice) == 4:
        sys.exit()


while True:
    # user_input = int(input("Enter your choice 1.login/2.register/3.exit:"))
    user_input = get_input("Enter your choice 1.login/2.register/3.forgot_password/4.exit :", check_loginchoice)
    welcome(user_input)
