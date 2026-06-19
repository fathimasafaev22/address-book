# Address Book Management System

## Project Overview

The Address Book Management System is a simple command-line application developed using Python and MySQL. It allows users to store and manage contact information efficiently. Users can add new contacts, view all contacts, search for a specific contact, and delete contacts from the database.

## Features

* Add new contacts
* View all saved contacts
* Search contacts by name
* Delete contacts
* Store contact information in a MySQL database
* Simple menu-driven interface

## Technologies Used

* Python
* MySQL
* MySQL Connector for Python

## Database Configuration

### Database Name

ADDRESSBOOK

### Table Name

contacts

### Table Structure

| Column  | Data Type                         |
| ------- | --------------------------------- |
| id      | INT (Primary Key, Auto Increment) |
| name    | VARCHAR(100)                      |
| phone   | VARCHAR(20)                       |
| email   | VARCHAR(100)                      |
| address | VARCHAR(255)                      |

## Installation

### 1. Install Required Package

```bash
pip install mysql-connector-python
```

### 2. Create Database

```sql
CREATE DATABASE ADDRESSBOOK;
```

### 3. Create Contacts Table

```sql
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255)
);
```

### 4. Configure Database Credentials

Update the MySQL connection details in the Python script:

```python
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your_password",
    database="ADDRESSBOOK"
)
```

### 5. Run the Program

```bash
python addressbook.py
```

## Menu Options

```text
1. Add
2. View
3. Search
4. Delete
5. Exit
```

## Example Usage

### Add Contact

```text
Enter your name: fathima
Enter your phone_no: 123456789
Enter your email: fathima@gmail.com
Enter your address: calicut
Contact added successfully
```

### Search Contact

```text
Enter your name to search: fathima
fathima - 123456789 - fathima@gmail.com - calicut
```

### Delete Contact

```text
Enter your name to delete: fathima
Contact deleted successfully
```

## Project Workflow

1. Connect to the MySQL database.
2. Display the menu options.
3. Perform CRUD operations:

   * Create (Add Contact)
   * Read (View Contacts)
   * Search Contact
   * Delete Contact
4. Save changes in the database.
5. Exit the application.

## Future Improvements

* Update existing contacts
* Validate phone numbers and email addresses
* Search using phone number or email
* Build a graphical user interface (GUI)
* Export contacts to CSV or Excel

## Author

Fathima Safa
