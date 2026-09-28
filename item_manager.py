from data_manager import ITEMS_FILE, load_data, save_data
from utils import get_next_id


def add_item(username):
    items = load_data(ITEMS_FILE)

    print("\n===== Add Item =====")
    item_type = input("Enter type (Lost/Found): ").strip().title()

    if item_type not in ["Lost", "Found"]:
        print("Please enter only Lost or Found.")
        return

    name = input("Enter item name: ").strip()
    description = input("Enter description: ").strip()
    location = input("Enter location: ").strip()
    date = input("Enter date (DD-MM-YYYY): ").strip()

    if name == "" or location == "":
        print("Item name and location are required.")
        return

    item = {
        "id": get_next_id(items),
        "type": item_type,
        "name": name,
        "description": description,
        "location": location,
        "date": date,
        "reported_by": username,
        "status": "Open"
    }

    items.append(item)
    save_data(ITEMS_FILE, items)

    print("Item added successfully. Item ID:", item["id"])


def view_items():
    items = load_data(ITEMS_FILE)

    print("\n===== All Items =====")

    if len(items) == 0:
        print("No items found.")
        return

    for item in items:
        print_item(item)


def print_item(item):
    print("--------------------------------")
    print("ID:", item["id"])
    print("Type:", item["type"])
    print("Name:", item["name"])
    print("Description:", item["description"])
    print("Location:", item["location"])
    print("Date:", item["date"])
    print("Reported by:", item["reported_by"])
    print("Status:", item["status"])


def find_item(items, item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None


def update_item(username):
    items = load_data(ITEMS_FILE)

    try:
        item_id = int(input("Enter item ID to update: "))
    except ValueError:
        print("Please enter a number.")
        return

    item = find_item(items, item_id)

    if item is None:
        print("Item not found.")
        return

    if item["reported_by"] != username:
        print("You can update only your own item.")
        return

    print("Leave a field empty to keep the old value.")

    name = input("New name: ").strip()
    location = input("New location: ").strip()
    description = input("New description: ").strip()

    if name:
        item["name"] = name
    if location:
        item["location"] = location
    if description:
        item["description"] = description

    save_data(ITEMS_FILE, items)
    print("Item updated successfully.")


def delete_item(username):
    items = load_data(ITEMS_FILE)

    try:
        item_id = int(input("Enter item ID to delete: "))
    except ValueError:
        print("Please enter a number.")
        return

    item = find_item(items, item_id)

    if item is None:
        print("Item not found.")
        return

    if item["reported_by"] != username:
        print("You can delete only your own item.")
        return

    items.remove(item)
    save_data(ITEMS_FILE, items)
    print("Item deleted successfully.")


def mark_as_found(username):
    items = load_data(ITEMS_FILE)

    try:
        item_id = int(input("Enter item ID: "))
    except ValueError:
        print("Please enter a number.")
        return

    item = find_item(items, item_id)

    if item is None:
        print("Item not found.")
        return

    item["status"] = "Returned"
    item["returned_by"] = username

    save_data(ITEMS_FILE, items)
    print("Item marked as returned.")
