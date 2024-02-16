# Create tables in the DB

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# Here we are creating two table have three columns with the type of column using the commands of SQL language
cursor.execute('CREATE TABLE movies(title TEXT, genre TEXT, year INTEGER)')
cursor.execute('CREATE TABLE users(name TEXT, email TEXT, age INTEGER)')

# We need to close the connection of DB
con.close()
