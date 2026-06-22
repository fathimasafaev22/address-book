import mysql.connector

mydb = mysql.connector.connect(
    host="host",
    user="user",
    password="pass",
    database="ADDRESSBOOK"
)

cursor = mydb.cursor()

address_book = []

def Add_contact():
    name = input("Enter your name: ")
    phone = input("Enter your phone_no: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    sql = """
    INSERT INTO contacts(name, phone, email, address)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (name, phone, email, address))
    mydb.commit()

    print("Contact added successfully")



def view():
    cursor.execute("SELECT * FROM contacts")
    records = cursor.fetchall()

    for row in records:
        print(row[1], "-", row[2], "-", row[3], "-", row[4])


def search():
    name = input("Enter your name to search: ")

    cursor.execute(
        "SELECT * FROM contacts WHERE name=%s",

        (name,)
    )

    result = cursor.fetchone()

    if result:
        print(result[1], "-", result[2], "-", result[3], "-", result[4])
    else:
        print("Contact not found")


def delete():
    name = input("Enter your name to delete: ")

    cursor.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )

    mydb.commit()

    if cursor.rowcount > 0:
        print("Contact deleted successfully")
    else:
        print("Contact not found")


while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        Add_contact()
    elif choice == "2":
        view()
    elif choice == "3":
        search()
    elif choice == "4":
        delete()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Not found.\n")
