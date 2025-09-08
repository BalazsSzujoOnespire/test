import psycopg2;

# Connect to the default 'postgres' database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
conn.autocommit = True
cursor = conn.cursor()

# Create a new empty database
cursor.execute("CREATE DATABASE test;")

cursor.close()
conn.close()