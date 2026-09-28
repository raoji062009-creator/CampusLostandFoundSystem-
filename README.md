# Campus Lost & Found System

A beginner-friendly **Python terminal project** for managing lost and found items on a college campus.

## Overview

The system gives students and staff a simple way to report lost or found items and search existing reports.

The project uses **JSON files** instead of a database, which keeps the project simple and suitable for learning Python.

## Features

- User registration
- User login
- Add lost item
- Add found item
- View all items
- Search items
- Update your own item
- Delete your own item
- Mark an item as returned
- Simple statistics/report
- Input validation
- Basic automated tests

## Technologies Used

- Python 3
- JSON
- Python standard library
- Terminal / Command Prompt
- unittest for basic testing

No external Python packages are required.

## Project Structure

```text
Campus_Lost_and_Found_System/
│
├── main.py
├── auth.py
├── data_manager.py
├── item_manager.py
├── search.py
├── reports.py
├── utils.py
├── test_project.py
├── statement.md
├── README.md
│
└── data/
    ├── users.json
    └── items.json
```

## Main Modules

### 1. User Management
File: `auth.py`

Handles registration and login.

### 2. Data Management
File: `data_manager.py`

Creates and reads the JSON files used by the project.

### 3. Item Management
File: `item_manager.py`

Handles adding, viewing, updating, deleting and returning items.

### 4. Search
File: `search.py`

Searches item names, descriptions and locations.

### 5. Reports
File: `reports.py`

Displays basic project statistics.

### 6. Utilities
File: `utils.py`

Contains small helper functions such as generating the next item ID.

## How to Run

### Step 1 - Install Python

Install Python 3 on your computer.

Check the installation:

```bash
python --version
```

On some systems you may need:

```bash
python3 --version
```

### Step 2 - Open the project folder

Open Command Prompt or Terminal inside the project folder.

### Step 3 - Run the program

```bash
python main.py
```

or:

```bash
python3 main.py
```

The `data` folder and JSON files are created automatically when the program starts.

## How to Test

Run:

```bash
python -m unittest test_project.py
```

Expected result:

```text
..
----------------------------------------------------------------------
Ran 2 tests in ...
OK
```

## Example Workflow

1. Start the program.
2. Register a username and password.
3. Login.
4. Choose `1` to add a lost or found item.
5. Enter item details.
6. Choose `3` to search for an item.
7. If an item is returned, choose `6` and enter its ID.
8. Use `7` to see the project report.

## Data Storage

The project stores data locally:

- `data/users.json` stores user accounts.
- `data/items.json` stores item reports.

Example item:

```json
{
    "id": 1,
    "type": "Lost",
    "name": "Student ID Card",
    "description": "Blue college ID card",
    "location": "Library",
    "date": "28-09-2026",
    "reported_by": "student1",
    "status": "Open"
}
```

## Limitations

This is an educational beginner project.

- It works only in the terminal.
- It does not use an online database.
- It does not send notifications.
- Passwords are stored in plain text.
- There are no administrator accounts.
- It does not automatically verify whether a person owns an item.

## Future Enhancements

- SQLite database
- Admin login
- Better password security
- Image upload for items
- Email or notification system
- Web interface using Flask
- Better matching between lost and found reports
- Date-based filtering

## Learning Outcomes

This project demonstrates:

- Variables and data types
- Functions
- Lists and dictionaries
- Conditional statements
- Loops
- File handling
- JSON
- Modular programming
- Input validation
- CRUD operations
- Basic unit testing

## Author

Student Project - VITyarthi
