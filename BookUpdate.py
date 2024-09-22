from Database import (show_all_books, book_borrow, book_count_update,
                      book_return,all_bookborrow_records,show_all_users,update_overdue_charges)
from datetime import datetime

def book_Checkout(title_value, email):

    re_str = ''
    userid =""
    for user in show_all_users():
        if user.get("user_email") == email:
            userid = user.get("user_id")
            break
        else:
            userid = None

    eligible_user = True
    for details in all_bookborrow_records():
        if details.get("user_id") == userid and  details.get("return_date") is None:
            eligible_user = False
        else:
            eligible_user = True

    book_ls = show_all_books()
    for item in book_ls:
        if item["title"] == title_value and eligible_user is True:
            if item.get("book_count") >= 1:
                book_borrow(item.get("book_id"), email)
                book_count_update(item.get("book_id"), item.get("book_count") - 1)
                re_str = "you have checkout book successfully"
                break

            else:
                re_str = "Book is not available.Book count is 0"
                break
        else:
            re_str = "Enter Book Name Correctly or may be user already check in some book"
    print(re_str)


# book_Checkout("Don Quixote", "user@gmail.com")

def Book_Return(title_value, email):
    res_str = ""
    userid = ""
    # print()
    for user in show_all_users():
        if user.get("user_email") == email:
            userid = user.get("user_id")
            break
        else:
            userid = None

    return_date = None

    borrow_userid = ""
    borrow_bookid = ""
    borrow_id = ""
    for item in all_bookborrow_records():
        if item.get("return_date") is None and item.get("user_id") == userid:
            return_date = None
            borrow_userid = item.get("user_id")
            borrow_bookid = item.get("book_id")
            borrow_id = item.get("borrow_id")
            break

        else:
            return_date = item.get("return_date")



    for item in show_all_books():
        if item["title"] == title_value:
            if item.get("book_id") == borrow_bookid and return_date is None and userid == borrow_userid:
                book_return(item.get("book_id"),email)
                book_count_update(item.get("book_id"), item.get("book_count") + 1)
                res_str = "you have return the  book .Thank you !"
                update_overdue_charges(datetime.now(),borrow_id)
                break
            else:
                res_str = "Book already return by user"
        else:
            res_str = "Enter Book Name correctly or may be user already return the book!"
    print(res_str)
# Book_Return("Alice'S Adventures In Wonderland","mousumi@gmail.com")
