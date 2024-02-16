# Read data from the table

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# Here we select the table and the fields from it
dataM = cursor.execute('SELECT rowid, * FROM movies')

# Here we use a for loop to print the fields
for row in dataM:
    print(row)

# We need to close the connection of DB
con.commit()
con.close()
