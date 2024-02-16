# Delete the tables or data

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# First line we delete the data using the DELETE command and WHERE to select a specific row
# Second line we selected our table to print it
cursor.execute('DELETE FROM movies WHERE title LIKE "oppenheimer" AND year IS NULL')
# To delete a whole table we are using
# cursor.execute('DROP TABLE movies')
cursor.execute('SELECT rowid, * FROM movies')

# We use a for loop to print all fields from the table
data = cursor.fetchall()
for row in data:
    print(row)

# We need to close the connection of DB
con.commit()
con.close()
