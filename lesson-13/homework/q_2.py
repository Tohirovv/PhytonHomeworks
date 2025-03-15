import sqlite3

def task2():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    # Create Books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    """)

    # Check if data already exists before inserting to avoid duplicates
    cursor.execute("SELECT COUNT(*) FROM Books")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
        """, [
            ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
            ("1984", "George Orwell", 1949, "Dystopian"),
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
        ])
    
    # Commit before modifying the structure
    conn.commit()
    
    # Update Year_Published for "1984"
    cursor.execute("""
        UPDATE Books SET Year_Published = 1950 WHERE Title = "1984"
    """)
    
    # Query: Retrieve Title and Author of Dystopian books
    cursor.execute("""
        SELECT Title, Author FROM Books WHERE Genre = "Dystopian"
    """)
    print("Dystopian Books:", cursor.fetchall())

    # Delete books published before 1950
    cursor.execute("""
        DELETE FROM Books WHERE Year_Published < 1950
    """)
    
    # Add Rating column (check if it already exists to avoid errors)
    try:
        cursor.execute("""
            ALTER TABLE Books ADD COLUMN Rating REAL
        """)
    except sqlite3.OperationalError:
        pass  # Column already exists
    
    # Update Rating values
    cursor.executemany("""
        UPDATE Books SET Rating = ? WHERE Title = ?
    """, [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ])
    
    # Retrieve all books sorted by Year_Published ascending
    cursor.execute("""
        SELECT * FROM Books ORDER BY Year_Published ASC
    """)
    print("Sorted Books:", cursor.fetchall())
    
    conn.commit()
    conn.close()
