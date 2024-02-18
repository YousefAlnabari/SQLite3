# Insert rows/data into the tables/DB many data

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# Here we are creating a list of data to insert in the next step
movies = [
    ('the godfather', 'crime', 1970),
    ('oppenheimer', 'drama', 2023),
    ('the whale', 'drama', 2023),
    ('delete history', 'comedy', 2020),
    ('apples', 'fantasy', 2020)
]

# Here we add many rows/data inside table/DB
cursor.executemany("INSERT INTO movies VALUES(?,?,?)", movies)

# We need to close the connection of DB
con.commit()
con.close()
