from Database import search_book_bytitle


def Search_Book(book_list, title_value):
    re_str = ""
    result_book = search_book_bytitle(title_value)
    # print(result_book)
    # for item in book_list:
    if result_book is not None:
        if result_book.get("title") == title_value and result_book.get("book_count") > 0:
            # return item
            re_str = "Book is available"
            # break
        else:
            re_str = "Book is not available book count 0"
    else:
        re_str = "Book does not exist"
    print(re_str)
