import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_NAME = os.getenv("DB_NAME", "property_management")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)

conn = psycopg2.connect(
    dbname="postgres",
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
conn.autocommit = True
cur = conn.cursor()

try:
    cur.execute(f"CREATE DATABASE {DB_NAME} OWNER {DB_USER};")
    print(f"Database '{DB_NAME}' created successfully.")
except Exception as e:
    print(f"Database '{DB_NAME}' already exists or error occurred: {e}")

cur.close()
conn.close()

print(f"Database '{DB_NAME}' is ready / verified.")
