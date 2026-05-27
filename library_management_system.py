# ============================================================
#          LIBRARY MANAGEMENT SYSTEM
#          PYTHON + MYSQL PROJECT
# ============================================================

# INSTALL FIRST:
# pip install mysql-connector-python

import mysql.connector

# ============================================================
# MYSQL CONNECTION
# ============================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="navneetsql"
)

cursor = db.cursor()

# ============================================================
# CREATE DATABASE
# ============================================================

cursor.execute("CREATE DATABASE IF NOT EXISTS library_management")

cursor.execute("USE library_management")

# ============================================================
# CREATE TABLES
# ============================================================

# ---------------- BOOKS TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    book_id INT PRIMARY KEY,
    book_name VARCHAR(100),
    book_author VARCHAR(100),
    publishing_year INT,
    book_type VARCHAR(50)
)
""")

# ---------------- STUDENTS TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    student_class VARCHAR(50),
    birth_year INT,
    phone_number VARCHAR(20)
)
""")

# ---------------- AUTHORS TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(100),
    author_book_name VARCHAR(100),
    publishing_year INT,
    total_books_published INT,
    author_phone VARCHAR(20)
)
""")

# ---------------- ISSUED BOOKS TABLE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books(
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    book_name VARCHAR(100),
    book_author VARCHAR(100),
    issued_to_student VARCHAR(100)
)
""")

db.commit()

# ============================================================
# REGISTER BOOK
# ============================================================

def register_book():

    print("\n========== REGISTER BOOK ==========")

    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    book_author = input("Enter Book Author: ")
    publishing_year = int(input("Enter Publishing Year: "))
    book_type = input("Enter Book Type: ")

    query = """
    INSERT INTO books
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (
        book_id,
        book_name,
        book_author,
        publishing_year,
        book_type
    )

    cursor.execute(query, values)

    db.commit()

    print("Book Registered Successfully")

# ============================================================
# REGISTER STUDENT
# ============================================================

def register_student():

    print("\n========== REGISTER STUDENT ==========")

    student_name = input("Enter Student Name: ")
    student_id = int(input("Enter Student ID: "))
    student_class = input("Enter Student Class: ")
    birth_year = int(input("Enter Student Birth Year: "))
    phone_number = input("Enter Student Phone Number: ")

    query = """
    INSERT INTO students
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (
        student_id,
        student_name,
        student_class,
        birth_year,
        phone_number
    )

    cursor.execute(query, values)

    db.commit()

    print("Student Registered Successfully")

# ============================================================
# REGISTER AUTHOR
# ============================================================

def register_author():

    print("\n========== REGISTER AUTHOR ==========")

    author_name = input("Enter Author Name: ")
    author_book_name = input("Enter Author Book Name: ")
    publishing_year = int(input("Enter Publishing Year: "))
    total_books = int(input("Enter Total Books Published: "))
    author_phone = input("Enter Author Phone Number: ")
    author_id = int(input("Enter Author ID: "))

    query = """
    INSERT INTO authors
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    values = (
        author_id,
        author_name,
        author_book_name,
        publishing_year,
        total_books,
        author_phone
    )

    cursor.execute(query, values)

    db.commit()

    print("Author Registered Successfully")

# ============================================================
# ISSUE BOOK
# ============================================================

def issue_book():

    print("\n========== ISSUE BOOK ==========")

    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    book_author = input("Enter Book Author Name: ")
    student_name = input("Issued To Student Name: ")

    query = """
    INSERT INTO issued_books
    (book_id,book_name,book_author,issued_to_student)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        book_id,
        book_name,
        book_author,
        student_name
    )

    cursor.execute(query, values)

    db.commit()

    print("Book Issued Successfully")

# ============================================================
# ADD STUDENT DATA
# ============================================================

def add_student_data():

    print("\n========== ADD STUDENT DATA ==========")

    student_name = input("Enter Student Name: ")
    student_id = int(input("Enter Student ID: "))
    birth_year = int(input("Enter Student Birth Year: "))
    admission_year = int(input("Enter Admission Year: "))
    phone_number = input("Enter Student Phone Number: ")

    query = """
    INSERT INTO students
    (student_id,student_name,student_class,birth_year,phone_number)
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (
        student_id,
        student_name,
        admission_year,
        birth_year,
        phone_number
    )

    cursor.execute(query, values)

    db.commit()

    print("Student Data Added Successfully")

# ============================================================
# DELETE BOOK DATA
# ============================================================

def delete_book_data():

    print("\n========== DELETE BOOK DATA ==========")

    book_id = int(input("Enter Book ID To Delete: "))

    query = """
    DELETE FROM books
    WHERE book_id=%s
    """

    values = (book_id,)

    cursor.execute(query, values)

    db.commit()

    print("Book Deleted Successfully")

# ============================================================
# DELETE STUDENT DATA
# ============================================================

def delete_student_data():

    print("\n========== DELETE STUDENT DATA ==========")

    student_id = int(input("Enter Student ID To Delete: "))

    query = """
    SELECT * FROM students
    WHERE student_id=%s
    """

    values = (student_id,)

    cursor.execute(query, values)

    student = cursor.fetchone()

    if student:

        print("Student Name :", student[1])

        query = """
        DELETE FROM students
        WHERE student_id=%s
        """

        values = (student_id,)

        cursor.execute(query, values)

        db.commit()

        print("Student Data Deleted Successfully")

    else:
        print("Student Not Found")

# ============================================================
# SHOW BOOKS
# ============================================================

def show_books():

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    print("\n========== BOOK RECORDS ==========")

    for book in books:

        print("\nBook ID :", book[0])
        print("Book Name :", book[1])
        print("Book Author :", book[2])
        print("Publishing Year :", book[3])
        print("Book Type :", book[4])

# ============================================================
# SHOW STUDENTS
# ============================================================

def show_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n========== STUDENT RECORDS ==========")

    for student in students:

        print("\nStudent ID :", student[0])
        print("Student Name :", student[1])
        print("Student Class :", student[2])
        print("Birth Year :", student[3])
        print("Phone Number :", student[4])

# ============================================================
# SHOW AUTHORS
# ============================================================

def show_authors():

    cursor.execute("SELECT * FROM authors")

    authors = cursor.fetchall()

    print("\n========== AUTHOR RECORDS ==========")

    for author in authors:

        print("\nAuthor ID :", author[0])
        print("Author Name :", author[1])
        print("Book Name :", author[2])
        print("Publishing Year :", author[3])
        print("Total Books Published :", author[4])
        print("Author Phone :", author[5])

# ============================================================
# SHOW ISSUED BOOKS
# ============================================================

def show_issued_books():

    cursor.execute("SELECT * FROM issued_books")

    books = cursor.fetchall()

    print("\n========== ISSUED BOOK RECORDS ==========")

    for book in books:

        print("\nIssue ID :", book[0])
        print("Book ID :", book[1])
        print("Book Name :", book[2])
        print("Book Author :", book[3])
        print("Issued To :", book[4])

# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print("\n=================================================")
    print("        WELCOME TO LIBRARY MANAGEMENT SYSTEM")
    print("=================================================")

    print("1. Register Books")
    print("2. Register Students")
    print("3. Register Authors")
    print("4. Show Books")
    print("5. Show Students")
    print("6. Issued Books")
    print("7. Add Student Data")
    print("8. Delete Book Data")
    print("9. Delete Student Data")
    print("10. Show Authors")
    print("11. Show Issued Books")
    print("12. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        register_book()

    elif choice == "2":
        register_student()

    elif choice == "3":
        register_author()

    elif choice == "4":
        show_books()

    elif choice == "5":
        show_students()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        add_student_data()

    elif choice == "8":
        delete_book_data()

    elif choice == "9":
        delete_student_data()

    elif choice == "10":
        show_authors()

    elif choice == "11":
        show_issued_books()

    elif choice == "12":

        print("Thank You For Using Library Management System")

        db.close()

        break

    else:
        print("Invalid Choice")
