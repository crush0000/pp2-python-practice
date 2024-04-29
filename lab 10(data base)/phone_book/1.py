# SQL

# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='lab10', 
    user='postgres', 
    password='Aldiayr2005@',
    port='5433'
    )

# Create a cursor to work with the database
cur = conn.cursor()


# Create a new table
cur.execute("""CREATE TABLE phone_book (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")

conn.commit()

