import sqlite3

def task1():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()
    
    # Create Roster table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)
    
    # Insert data
    cursor.executemany("""
        INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
    """, [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ])
    
    # Update Name of Jadzia Dax to Ezri Dax
    cursor.execute("""
        UPDATE Roster SET Name = "Ezri Dax" WHERE Name = "Jadzia Dax"
    """)
    
    # Query: Retrieve Name and Age of Bajoran species
    cursor.execute("""
        SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
    """)
    print("Bajoran Characters:", cursor.fetchall())
    
    # Delete characters older than 100 years
    cursor.execute("""
        DELETE FROM Roster WHERE Age > 100
    """)
    
    # Add Rank column
    cursor.execute("""
        ALTER TABLE Roster ADD COLUMN Rank TEXT
    """)
    
    # Update Rank values
    cursor.executemany("""
        UPDATE Roster SET Rank = ? WHERE Name = ?
    """, [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ])
    
    # Retrieve all characters sorted by Age descending
    cursor.execute("""
        SELECT * FROM Roster ORDER BY Age DESC
    """)
    print("Sorted Roster:", cursor.fetchall())
    
    conn.commit()
    conn.close()
