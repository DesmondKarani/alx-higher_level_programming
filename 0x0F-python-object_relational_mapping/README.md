# Object-Relational Mapping (ORM) with Python, MySQL, and SQLAlchemy

This project aims to bridge two powerful worlds in software development: databases and Python programming. By leveraging the capabilities of MySQL and SQLAlchemy, this project demonstrates how to efficiently interact with a database using Python's Object-Oriented Programming (OOP) paradigms without writing complex SQL queries.

## Project Overview

The project is divided into two main parts:

1. **Using MySQLdb to Connect to MySQL Database**: The initial phase involves direct database operations using the MySQLdb module, executing SQL queries from a Python script.

2. **Adopting SQLAlchemy for ORM**: The second phase transitions to using SQLAlchemy, an Object-Relational Mapper that abstracts SQL queries into Python code, focusing on object manipulation rather than database operations.

### Objectives

- Understand and apply Python's OOP principles.
- Connect to a MySQL database from Python.
- Perform CRUD operations on a MySQL database from Python.
- Grasp the concept and advantages of using an ORM.
- Map Python classes to MySQL tables using SQLAlchemy.
- Create and manage a Python Virtual Environment.

## Prerequisites

- Python 3.8.5
- Ubuntu 20.04 LTS
- MySQL 8.0
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x

## Setup and Installation

### Python Virtual Environment

```bash
sudo apt-get install python3.8-venv
python3 -m venv venv
source venv/bin/activate
```

### MySQLdb Installation

Ensure MySQL is installed and configured before proceeding.

```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient
```

### SQLAlchemy Installation

```bash
sudo pip3 install SQLAlchemy
```

## Usage

### Without ORM (Using MySQLdb)

```python
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="my_db")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### With ORM (Using SQLAlchemy)

```python
from sqlalchemy import create_engine, Session
from my_model import Base, State

engine = create_engine('mysql+mysqldb://root:root@localhost/my_db', pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
session.close()
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Special thanks to Guillaume for the project guidance.
- Hat tip to anyone whose code was used as inspiration.
