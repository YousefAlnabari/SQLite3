# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# We need to close the connection of DB
con.close()
