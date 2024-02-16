# Insert row/data into the tables/DB

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# Here we add row/data inside tables/DB with the same idea of parameters on functions
cursor.execute('INSERT INTO movies(title, genre) VALUES("oppenheimer", "drama")')
# Here we insert the data without specific columns for all columns
cursor.execute('INSERT INTO users VALUES("Yousef", "example@email.com", 17)')

# We need to close the connection of DB
con.close()
