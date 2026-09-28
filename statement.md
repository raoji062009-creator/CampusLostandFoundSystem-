# Campus Lost & Found System - Project Statement

## 1. Problem Statement

In a college campus, students and staff can lose or find personal items such as ID cards, books, bags, wallets, keys and other belongings. In many cases, information about these items is shared through informal messages or announcements, which can make it difficult to find the correct item.

The **Campus Lost & Found System** is a simple terminal-based Python application that provides one place to report lost or found items, search for items, update information and mark items as returned.

## 2. Scope of the Project

The project is designed for a college campus and works through the terminal.

The system covers:

- User registration and login
- Adding lost and found item reports
- Viewing all reported items
- Searching for an item
- Updating an item
- Deleting an item
- Marking an item as returned
- Showing a simple summary report
- Storing data in JSON files

The project does not include a web application, mobile application, online database or real-time notifications.

## 3. Target Users

- College students
- Teaching staff
- Non-teaching staff
- Campus help-desk or lost-and-found staff

## 4. High-Level Features

### Module 1 - User Management
- Register a new user
- Login using username and password

### Module 2 - Item Management
- Add lost/found item
- View items
- Update own item
- Delete own item
- Mark an item as returned

### Module 3 - Search
- Search by item name
- Search by description
- Search by location

### Module 4 - Reports
- Count total items
- Count lost items
- Count found items
- Count open items
- Count returned items

## 5. Functional Requirements

1. The system shall allow a user to register.
2. The system shall allow a registered user to login.
3. The system shall allow a logged-in user to add an item.
4. The system shall allow users to view reported items.
5. The system shall allow users to search for items.
6. The system shall allow a user to update their own item.
7. The system shall allow a user to delete their own item.
8. The system shall allow an item to be marked as returned.
9. The system shall display a basic report.

## 6. Non-Functional Requirements

### Usability
The program should use simple menus and clear terminal messages.

### Reliability
The application should save item and user information in JSON files so the information remains after the program closes.

### Error Handling
Invalid menu choices, empty required fields and invalid numeric input should be handled without crashing the program.

### Maintainability
The project is divided into multiple Python files so that each part is easier to understand and modify.

### Resource Efficiency
The project uses Python standard library modules and small JSON files. No external package is required.

### Security
Basic login checking is included. This is an educational project, so passwords are stored simply in a local JSON file and are not intended for production use.

## 7. Expected Outcome

The expected outcome is a working beginner-friendly terminal application that demonstrates Python programming, functions, file handling, JSON storage, validation, CRUD operations and basic testing.
