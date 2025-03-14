import sqlite3

insert = """
    Insert into Roster Values('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29);
"""
with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    con.execute("drop table if exists Roster;")
    query = "Create table Roster(Name text, Species text, Age int);"
    query2 = "Select * from Roster order by age desc"
    
    data = cursor.execute(query)
    con.execute(insert)
    con.execute("UPDATE Roster SET Name='Ezri Dax' WHERE Name= 'Jadzia Dax'")
    data3 = con.execute(query2)
    data2 = con.execute("Select Name, Age from Roster WHERE Species = 'Bajoran'")
    con.execute("Delete from Roster WHERE Age>100")
    con.execute("ALTER TABLE Roster ADD column Rank TEXT")
    con.execute("Update Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
    con.execute("Update Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
    con.execute("Update Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")
print(data3.fetchall())
print(data2.fetchall())