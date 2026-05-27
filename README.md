Library Management System – Project Description

The Library Management System is a Python-based mini project developed using Python and MySQL for managing library operations digitally. This project helps librarians efficiently maintain records of books, students, authors, and issued books through a menu-driven console application.

The system establishes a connection with a MySQL database using the mysql.connector module and automatically creates the required database and tables if they do not already exist. It provides different functionalities such as book registration, student registration, author registration, issuing books, displaying records, and deleting records.

Main Features:
Add and manage book records
Register student details
Store author information
Issue books to students
Display all records from database tables
Delete book and student data
Automatic database and table creation
Menu-driven user interface
Technologies Used:
Programming Language: Python
Database: MySQL
Connector Library: mysql-connector-python
Database Tables:
Books Table
Stores book ID, name, author, publishing year, and category.
Students Table
Stores student details such as ID, name, class, birth year, and phone number.
Authors Table
Maintains author-related information and published books.
Issued Books Table
Keeps records of books issued to students.
Working of the Project:

When the program starts, it connects to MySQL and creates the database named library_management. After that, all required tables are created automatically. The user is shown a menu where different operations can be selected. Based on the user’s choice, the system performs database operations like inserting, fetching, updating, or deleting records.

This project demonstrates the practical implementation of:

Python functions
MySQL database handling
CRUD operations
User input handling
Menu-driven programming
Advantages:
Reduces manual record keeping
Easy to maintain library data
Fast data retrieval
Beginner-friendly database project
Useful for school and college mini projects
Conclusion:

The Library Management System is a simple yet powerful database management project that automates basic library operations. It is suitable for beginners who want to learn Python database connectivity and real-world CRUD applications using MySQL.
