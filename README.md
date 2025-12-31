# Property Management API

This is a simple REST API project for managing apartments, chores (utility services), and payments. Built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **Alembic**.

---

## Installation

### Clone the repository

```
git clone <your-repo-url> cd db_final_project
```

### Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Configure environment variables

Create a .env file in the root of the project with:

```
DB_USER=postgres
DB_PASSWORD=1234
DB_NAME=utility_payments
DB_HOST=localhost
DB_PORT=5432

DB_SUPERUSER=postgres
DB_SUPERUSER_PASSWORD=postgres
```

Make sure the user exists in PostgreSQL and has permission to create databases.

Make sure `DB_SUPERUSER_PASSWORD` matches the PostgreSQL superuser password.

## Database Initialization and Populate Data

Before running the API for the first time, you should create the database and populate it with some initial data.

### Create the database

Run the database creation script:

```
python create_db.py
```

This will:

- Create the `property_management` database if it doesn't exist

- Connect as superuser (`DB_SUPERUSER`)

- Set the owner to the user defined in `.env`

### Populate the database

Populate the database via REST API:

```
python scripts/populate.py
```

This will add sample:

- Chore types

- Apartments

- Payments

After this, the API is ready to use with test data.

## Running the Project

```
uvicorn app.main:app --reload
```

Visit API documentation at:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all CRUD endpoints for:

- Apartments

- Chore types

- Payments
