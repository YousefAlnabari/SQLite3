# Update the data

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# First line we update the data using the UPDATE command and WHERE to select a specific row
# Second line we selected our table to print it
cursor.execute('UPDATE users SET age = 18 WHERE name LIKE "yousef" ')
cursor.execute('SELECT rowid, * FROM users')

# We use a for loop to print all fields from the table
data = cursor.fetchall()
for row in data:
    print(row)

# We need to close the connection of DB
con.commit()
con.close()
