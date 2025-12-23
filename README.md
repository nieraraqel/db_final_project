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
python3 -m venv .venv source .venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

## Run the project

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
