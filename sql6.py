# Read data from the tables using fetch

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# Here we select the table and the fields from it
cursor.execute('SELECT rowid, * FROM movies')

# Here we use a fetch command to print the fields
print(cursor.fetchone())    # Using it to fetch one item
print(cursor.fetchmany(2))  # Using it to fetch many items
print(cursor.fetchall())    # Using it to fetch all items

# How we can make for inside fetchall()
data = cursor.execute('SELECT rowid, * FROM users')

users = data.fetchall()
for row in users:
    print(row[1])

# We need to close the connection of DB
con.commit()
con.close()
