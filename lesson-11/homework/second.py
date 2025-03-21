import sqlite3
from aifc import Error


#create

def CreateTable(cursor):
    cursor.executescript("""
    DROP TABLE IF EXISTS library;
    CREATE TABLE library (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
    )
    """)

#insert

def Insert(cursor):
    data = (
        ("To kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F.Scott Fitzgerald", 1925, "Classic")
    )
    cursor.executemany("INSERT INTO library VALUES (?, ?, ?, ?)", data)

#update

def Update(cursor):
    cursor.execute("UPDATE library SET Year_Published = ? WHERE Year_Published = ?", (1950, 1984))

#query

def Query(cursor):
    result = cursor.execute("SELECT * FROM library WHERE Genre = ?", ("Dystopian",))
    for row in result:
        print(row)

#delete

def Delete(cursor):
    cursor.execute("DELETE FROM library WHERE Year_Published <= 1950")

#add column and update

def add_column(cursor):
    cursor.execute("ALTER TABLE library ADD COLUMN Rating INTEGER")

def update_column(cursor):
    cursor.executemany("""
        UPDATE library SET Rating = ? WHERE Title = ?;
    """, (
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ))

#advanced query

def advanced_query(cursor):
    result = cursor.execute("SELECT * FROM library ORDER BY Year_Published ASC")
    for row in result:
        print(row)

#main

def main():
    print("""
    1. Create table
    2. Insert data
    3. Update data
    4. Query data
    5. Delete data
    6. Add column
    7. Update column
    8. Advanced Query data
    """)
while(True):
    with sqlite3.connect("library.db") as connection:
        c = connection.cursor()
        choice = input("Enter your choice: ")
        if choice == "1":
            CreateTable(c)
        elif choice == "2":
            Insert(c)
        elif choice == "3":
            Update(c)
        elif choice == "4":
            Query(c)
        elif choice == "5":
            Delete(c)
        elif choice == "6":
            add_column(c)
        elif choice == "7":
            update_column(c)
        elif choice == "8":
            advanced_query(c)
        else:
            print("Invalid choice")
            break
        connection.commit()

if __name__ == "__main__":
    main()



