from Database import remove_book
def Book_Remove(book_list,title_value):
    remove_book(title_value)
    result_str = ""
    for item in book_list:
        if item["title"] == title_value:
            book_list.remove(item)
            result_str= "Book removed successfully"
        else:
            result_str = "Book doesn't exist !!!"
    print(result_str)
# Book_Remove(book_list,"Don Quixote")
