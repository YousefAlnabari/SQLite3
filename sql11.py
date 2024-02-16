# Fix some logical problems

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# To solve the run time problems we add IF NOT EXISTS
# We add three """ to write in multiple lines
# We add after the id of rows to make a automation id
cursor.execute('DROP TABLE movies')

cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT,
    year INTEGER
    )''')

cursor.execute('INSERT INTO movies(title, genre, year) VALUES("EXIT", "akshn", 2019)')
cursor.execute('SELECT rowid, * FROM movies')

# We use a for loop to print all fields from the table
data = cursor.fetchall()
for row in data:
    print(row)

# We need to close the connection of DB
con.commit()
con.close()
