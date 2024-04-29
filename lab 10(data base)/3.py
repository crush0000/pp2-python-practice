import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='lab10', 
    user='postgres', 
    password='Aldiyar2005@',
    port='5433'
    )

# Create a cursor to work with the database
cur = conn.cursor()


conn.commit()



cur.execute("""UPDATE phone_book
            SET phone_number = '+77778884411'
            WHERE id = '040504';
""")

conn.commit()