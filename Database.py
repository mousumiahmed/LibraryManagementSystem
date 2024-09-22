import mysql.connector
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost"
)


def create_database_and_tables(dbname):
    # global cursor
    global cursor
    try:

        if conn.is_connected():
            # print("Database connected successfully!")
            try:
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
                conn.commit()
                # print("Database created successfully!")
                conn.database = dbname
                user_table = """create table if not exists user_list (
                               user_id int primary key auto_increment,
                               user_name varchar(100) not null,
                               user_email varchar(100) unique not null,
                               user_type int not null,
                               password varchar(100) not null,
                               confirm_password varchar(100) not null,
                               profile_created timestamp default current_timestamp)"""
                book_table = """create table if not exists book_list (
                               book_id int primary key auto_increment,
                               title varchar(200) unique,
                               author varchar(100) not null,
                               isbn int ,
                               publication_date varchar(100),
                               book_count int check(book_count>=0),
                               created_by varchar(100) not null) auto_increment = 100"""
                # check_in_date = datetime.now()
                # due_date = datetime.now()+timedelta(days=15)
                book_borrow_table = """create table if not exists book_borrow_record (
                               borrow_id int primary key auto_increment,
                               book_id int,
                               user_id int,
                               check_in_date date not null,
                               return_due_date date not null,
                               return_date date ,
                               overdue_charges decimal(10,2) default 0,
                               foreign key(book_id) references book_list(book_id),
                               foreign key(user_id) references user_list(user_id)
                               ) auto_increment = 100"""
                admin_list = '''create table if not exists admin_details(
                                id varchar(50) primary key,
                                active_userid varchar(50),
                                foreign key(active_userid) references user_list(user_email)
                                )
                                '''
                cursor.execute(user_table)
                cursor.execute(book_table)
                cursor.execute(book_borrow_table)
                cursor.execute(admin_list)
                # print("Table  created successfully")
                conn.commit()
            except mysql.connector.Error as e:
                print(f"Error creating database: {e}")
                conn.rollback()
            finally:
                cursor.close()

    except Exception as e:
        print(f"Error connecting to MySQL: {e}")


create_database_and_tables("library_management_system")


def insert_user(user):
    # print(user)
    user_data = tuple(user.values())
    cursor = conn.cursor()
    query = 'INSERT INTO user_list (user_name, user_email,user_type,password,confirm_password) VALUES (%s,%s,%s,%s,%s)'
    cursor.execute(query, user_data)

    cursor.close()


# tp = ("Sjnjn","h@gmail.com",2,"Mousui@123","Mousui@123")
# print(insert_user(tp))
def update_active_admin(email, admin_id):
    cursor = conn.cursor()
    update_admin_details = '''update admin_details set active_userid = %s where id = %s'''
    cursor.execute(update_admin_details, (email, admin_id))
    conn.commit()
    cursor.close()


def update_password(email, password):
    cursor = conn.cursor()
    update_query = '''update user_list set password = %s,confirm_password = %s where user_email = %s'''
    cursor.execute(update_query, (password, password, email))
    conn.commit()
    cursor.close()


def insert_books(books, created_by):
    books = tuple(books.values())
    created = (created_by,)
    book_data = books + created
    # final_book_data = tuple(book_data)
    # print(type(book_data))
    cursor = conn.cursor()
    query = '''INSERT INTO book_list 
    (title, author,isbn,publication_date,book_count,created_by) VALUES (%s,%s,%s,%s,%s,%s)'''
    cursor.execute(query, book_data)
    conn.commit()
    cursor.close()


# def insert_admin_ids(value):
#     cursor = conn.cursor()
#     insert_admin = '''insert into admin_details (id) values (%s)'''
#     cursor.executemany(insert_admin, value)
#     conn.commit()
#     cursor.close()
#
#
# id_values = [("a-234",), ("a-442",), ("a-305",), ("a-400",), ("a-450",)]
# insert_admin_ids(id_values)


def select_admin_list():
    cursor = conn.cursor(dictionary=True)
    query = '''select * from admin_details'''
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data


select_admin_list()


def remove_book(book_title):
    cursor = conn.cursor()
    query = '''delete from book_list where title = %s'''
    cursor.execute(query, (book_title,))
    conn.commit()
    cursor.close()


def show_all_books():
    cursor = conn.cursor(dictionary=True)
    query = '''select * from book_list '''
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    # cursor.close()


def show_all_users():
    cursor = conn.cursor(dictionary=True)
    query = '''select * from user_list '''
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    # cursor.close()


def search_book_bytitle(book_title):
    cursor = conn.cursor(dictionary=True)
    query = '''select * from book_list where title = %s'''
    cursor.execute(query, (book_title,))
    # conn.commit()
    result = cursor.fetchone()
    cursor.close()
    return result


# search_book_bytitle("Dgfvgh Dgfhg")


def all_bookborrow_records():
    cursor = conn.cursor(dictionary=True)
    query = '''select * from book_borrow_record '''
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def book_borrow(bookid, useremail):
    cursor = conn.cursor()
    check_in_date = datetime.now()
    due_date = datetime.now() + timedelta(days=15)
    user_id_qu = '''select user_id from user_list where user_email = %s'''
    cursor.execute(user_id_qu, (useremail,))
    userid = cursor.fetchone()
    # print(userid[0])
    query = """
                INSERT INTO book_borrow_record (book_id,user_id, check_in_date,return_due_date)
                SELECT %s, %s,%s,%s
                FROM user_list,book_list
                WHERE user_list.user_id = %s
                and book_list.book_id = %s
                and not exists (
                    select 1 
                    from book_borrow_record 
                    where user_id = %s 
                    and return_date is null
                );
                """
    cursor.execute(query, (bookid, userid[0], check_in_date, due_date, userid[0], bookid, userid[0]))
    # print(cursor.fetchall())
    conn.commit()
    cursor.close()


# book_borrow()


def book_count_update(bookid, bookcount):
    cursor = conn.cursor()
    query = '''update book_list set book_count = %s where book_id = %s'''
    cursor.execute(query, (bookcount, bookid))
    conn.commit()
    cursor.close()


def book_return(book_id, useremail):
    return_date = datetime.now()
    cursor = conn.cursor()
    user_id_qu = '''select user_id from user_list where user_email = %s'''
    cursor.execute(user_id_qu, (useremail,))
    userid = cursor.fetchone()
    # print(userid[0])

    cursor = conn.cursor()
    query = '''update book_borrow_record set return_date = %s where book_id = %s
     and user_id = %s and return_date is null  '''
    cursor.execute(query, (return_date, book_id, userid[0]))
    conn.commit()
    cursor.close()


def update_overdue_charges(return_date, id):
    cursor = conn.cursor()
    return_due_date = '''select return_due_date from book_borrow_record where borrow_id =%s'''
    # return_date = '''select return_date from book_borrow_record where return_date is not null'''
    cursor.execute(return_due_date, (id,))

    due_date_result = cursor.fetchone()
    # print(due_date_result[0])
    overdue_charges = '''select datediff(%s,%s) from book_borrow_record where borrow_id = %s'''
    charges = cursor.execute(overdue_charges, (return_date, due_date_result[0], id,))
    days_to_charge = cursor.fetchone()[0]
    charge_update_query = '''update book_borrow_record set overdue_charges = %s where borrow_id = %s'''
    update_charge = days_to_charge * 5
    cursor.execute(charge_update_query, (update_charge, id))
    conn.commit()
    cursor.close()

# borrow_id = 118
# update_overdue_charges('2024-09-28',borrow_id)
