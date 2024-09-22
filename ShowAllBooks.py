from Database import show_all_books
def show_all_book_details(ls):
    ds = show_all_books()
    for ite in ds:
        print (f"Book Name :", ite.get("title"), "Author :", ite.get("author"), "ISBN :", ite.get("isbn"), "Publication :", ite.get("publication_date"),"Book Count :", ite.get("book_count"))