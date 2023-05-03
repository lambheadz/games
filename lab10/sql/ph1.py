"""import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

current = connection.cursor()
sql = '''
        CREATE TABLE phonebook(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            number VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
connection.commit()
connection.close()"""

import psycopg2
from config import host, database, user, password

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor object for executing SQL queries
cur = conn.cursor()

# Create the phonebook table (if it doesn't already exist)
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
""")

# Add a new entry to the phonebook
cur.execute("""
    INSERT INTO phonebook (name, phone)
    VALUES (%s, %s)
""", ("John Smith", "555-1234"))

# Commit the transaction
conn.commit()

# Retrieve all entries from the phonebook
cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()

# Print the entries to the console
for row in rows:
    print(f"{row[0]}: {row[1]} - {row[2]}")

# Update an entry in the phonebook
cur.execute("""
    UPDATE phonebook
    SET phone = %s
    WHERE id = %s
""", ("555-5678", 1))

# Commit the transaction
conn.commit()

# Delete an entry from the phonebook
cur.execute("""
    DELETE FROM phonebook
    WHERE id = %s
""", (2,))

# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
