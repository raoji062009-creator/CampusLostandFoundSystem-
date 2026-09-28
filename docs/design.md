# Design Notes

## System Architecture

```text
+----------------------+
|       User           |
+----------+-----------+
           |
           v
+----------------------+
|      main.py         |
|   Terminal Menu      |
+----------+-----------+
           |
   +-------+-------+----------------+
   |       |       |                |
   v       v       v                v
 auth   item_manager  search      reports
   |       |       |                |
   +-------+-------+----------------+
           |
           v
+----------------------+
|   data_manager.py    |
+----------+-----------+
           |
           v
+----------------------+
|      JSON Files      |
| users.json/items.json|
+----------------------+
```

## Workflow

```text
Start
  |
  v
Login/Register
  |
  v
Main Menu
  |
  +--> Add Item
  |
  +--> View Items
  |
  +--> Search Items
  |
  +--> Update Item
  |
  +--> Delete Item
  |
  +--> Mark Returned
  |
  +--> Show Report
  |
  v
Logout
  |
  v
End
```

## Simple Data Design

### User

- username
- password

### Item

- id
- type
- name
- description
- location
- date
- reported_by
- status

## Functional Modules

1. User Management
2. Item Management / CRUD
3. Search
4. Reporting

## Basic Use Cases

**User -> Register**

**User -> Login**

**User -> Add Item**

**User -> View Items**

**User -> Search Items**

**User -> Update Own Item**

**User -> Delete Own Item**

**User -> Mark Item Returned**

**User -> View Report**
