import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_NAME = os.getenv("DB_NAME", "property_management")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
SUPERUSER = os.getenv("DB_SUPERUSER", "postgres")
SUPERUSER_PASSWORD = os.getenv("DB_SUPERUSER_PASSWORD", "postgres")

try:
    conn = psycopg2.connect(
        dbname="template1",
        user=SUPERUSER,
        password=SUPERUSER_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    print(f"Connected to PostgreSQL as superuser '{SUPERUSER}'")
except Exception as e:
    print("Error connecting to PostgreSQL:", e)
    exit(1)

try:
    cur.execute(f"CREATE USER {DB_USER} WITH PASSWORD '{DB_PASSWORD}';")
    print(f"User '{DB_USER}' created successfully")
except psycopg2.errors.DuplicateObject:
    print(f"User '{DB_USER}' already exists")

try:
    cur.execute(f"CREATE DATABASE {DB_NAME} OWNER {DB_USER};")
    print(f"Database '{DB_NAME}' created with owner '{DB_USER}'")
except psycopg2.errors.DuplicateDatabase:
    print(f"Database '{DB_NAME}' already exists")

cur.close()
conn.close()
print("Database initialization complete")
