#import library
import sqlite3


#connection
def connect_db():
    return sqlite3.connect('roster.db')


#Create
def create_table(cursor):
    create = """
    CREATE TABLE IF NOT EXISTS roster(
       Name TEXT,
       Species TEXT,
       Age INTEGER
    );
    """
    cursor.execute(create)




#Insert
def insert_data(cursor):
    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    cursor.executemany("INSERT OR IGNORE INTO roster (Name, Species, Age) VALUES (?, ?, ?);", data)


#Update
def update_name(cursor, old_name, new_name):
    cursor.execute("UPDATE roster SET Name = ? WHERE Name = ?", (new_name, old_name))


#Query
def query_species(cursor, species):
    result = cursor.execute("SELECT * FROM roster WHERE Species = ?", (species,))
    for row in result:
        print(f"name: {row[0]}, age: {row[2]}")


#Delete
def delete_old_entries(cursor):
    cursor.execute("DELETE FROM roster WHERE Age >= 100")


#Add column
def add_rank_column(cursor):
    cursor.execute("PRAGMA table_info(roster);")
    columns = [column[1] for column in cursor.fetchall()]

    if "Rank" not in columns:
        cursor.execute("ALTER TABLE roster ADD COLUMN Rank TEXT;")


#Update
def update_ranks(cursor):
    cursor.executemany("""
        UPDATE roster SET Rank = ? WHERE Name = ?;
    """, [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ])


#sort
def display_sorted_by_age(cursor):
    result = cursor.execute("SELECT * FROM roster ORDER BY Age DESC")
    for row in result:
        print(row)


#Main
def main():
    with connect_db() as c:
        cursor = c.cursor()

        #Call
        create_table(cursor)
        insert_data(cursor)
        update_name(cursor, "Jadzia Dax", "Ezri Dax")
        query_species(cursor, "Bajoran")
        delete_old_entries(cursor)
        add_rank_column(cursor)
        update_ranks(cursor)
        display_sorted_by_age(cursor)

        c.commit()



if __name__ == "__main__":
    main()
