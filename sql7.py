# Sort the data

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# Here we select the table and the fields from it and order it by title field
# You can add it after the field name DESC to reflect the sort, the default value is ASC
# And we can use a 'LIMIT 5', in this case, we will get the first 5 objects
cursor.execute('SELECT rowid, * FROM movies ORDER BY title')

# We use a for loop to print all fields from the table
movies = cursor.fetchall()
for row in movies:
    print(row)

# We need to close the connection of DB
con.commit()
con.close()
