# This simple database will store a budget program

import sqlite3
from unicodedata import category

# Connect to the database
connection = sqlite3.connect('budget.db')

# A cursor is an object which helps to execute the query and fetch the records from the database. The cursor plays a very important role in executing the query.
cursor = connection.cursor()

# Create table (if it does not already exist)

cursor.execute("CREATE TABLE IF NOT EXISTS budget (category TEXT, amount REAL)")

def get_category(cursor):
    cursor.execute("SELECT category FROM budget")
    
    # fetch all rows of a query result and return all rows as a list of tuples. Empty list returns if there is no record to fetch
    results = cursor.fetchall()
    if len(results) == 0:
        print("No categories in database")
        return None

    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0

    while choice < 1 or choice > len(results):
        choice = int(input("Category: "))
    return results[choice - 1][0]


    # User Dashboard Selection
choice = None
while choice != "6":

    print("1) Display Budget Sheet")
    print("2) Total Amount from Budget Sheet")
    print("3) Add Category")
    print("4) Update Amount in Budget")
    print("5) Delete Category")
    print("6) Quit")

    # user input
    choice = input("> ")
    print()
    
    if choice == "1":
        # display budget sheet
        cursor.execute("SELECT * FROM budget ORDER BY category DESC")

        print("{:>10}   {:>10}".format("category", "amount"))
        for record in cursor.fetchall():
            print("{:>10}   {:>10}".format(record[0], record[1]))

    elif choice == "2":
    # Display the total amount from budget sheet
        cursor.execute("SELECT SUM(amount) FROM budget")

        print("{:>10}".format("total amount"))
        for record in cursor.fetchall():
            print("{:>10}".format(record[0]))   

    elif choice == "3":
    # Add new category
        try:
            category = input("Category: ")
            amount = float(input("Amount: "))
            values = (category, amount)
            cursor.execute("INSERT INTO budget VALUES (?, ?)", values)
            connection.commit()
        except ValueError:
            print("Invalid amount!")
    elif choice == "4":
    # Update amount in category
        try:
            category = input("Category: ")
            amount = float(input("Amount: "))
            values = (amount, category)  # Make sure order is correct
            cursor.execute("UPDATE budget SET amount = ? WHERE category = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid category!")
        except ValueError:
            print("Invalid Amount!")
    elif choice == "5":
        # Delete category
        category = get_category(cursor)
        if category == None:
            continue
        values = (category, )
        cursor.execute("DELETE FROM budget WHERE category = ?", values)
        connection.commit()
    print()

# Close the database connection before exiting
connection.close()
        

        
         