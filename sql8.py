# The WHERE and LIKE commands

# We need to import an SQLite3 Lib
import sqlite3

# Here we are creating a file of a DB if he does not exist
con = sqlite3.connect('movies.db')

# Here we are creating a loop between the DB and SQL language
cursor = con.cursor()

# We can use the WHERE the same use if condition in other languages use = or != or > or < or >= or <=
# If we have multiple conditions we use an AND command or OR command
# And we have a UPPER or LOWER to convert the inputs or in conditions
# We use a LIKE command to equals between two texts without lower or upper cases condition
# We use a % to say maybe we have letters or no
# And if we add % before and after the letter or word letters to extract all the data have this letter
# If we use _ before or after the conditions on LIKE we have one letter before or after that connects where you are writing it
# We have a BETWEEN to git all the data between two values and the reflect commnd of between it's just add NOT before BETWEEN word
cursor.execute('SELECT rowid, * FROM movies WHERE title = LOWER("Oppenheimer") AND genre LIKE "_r%" AND rowid NOT BETWEEN 1 AND 2')

# We use a for loop to print all fields from the table
movies = cursor.fetchall()
for row in movies:
    print(row)

# We need to close the connection of DB
con.commit()
con.close()
