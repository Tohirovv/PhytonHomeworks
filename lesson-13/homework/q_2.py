import sqlite3

insert = """
    Insert into Books Values
    ('To Kill a Mockingbird', 'Harper Lee',	1960, 'Fiction'),
    ('1984', 'George Orwell', 1949,	'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald',	1925, 'Classic');
"""
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    con.execute("drop table if exists Roster;")
    query = "Create table Books(Title text, Author text, Year_Published int, Genre text);"
    query2 = "Select * from Books order by Year_Published"
    
    data = cursor.execute(query)
    con.execute(insert)
    con.execute("UPDATE Books SET Year_Published=1950 WHERE Title= '1984'")
    data3 = con.execute(query2)
    data2 = con.execute("Select Title, Author from Books WHERE Genre = 'Dystopian'")
    con.execute("Delete from Books WHERE Year_Published<1950")
    con.execute("ALTER TABLE Books ADD column Rating float")
    con.execute("Update Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
    con.execute("Update Books SET Rating = 4.7 WHERE Title = '1984'")
    con.execute("Update Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")
print(data3.fetchall())
print(data2.fetchall())