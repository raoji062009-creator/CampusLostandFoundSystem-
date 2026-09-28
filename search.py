from data_manager import ITEMS_FILE, load_data
from item_manager import print_item


def search_items():
    items = load_data(ITEMS_FILE)

    print("\n===== Search Items =====")
    keyword = input("Enter item name, location or description: ").strip().lower()

    if keyword == "":
        print("Please enter something to search.")
        return

    found = False

    for item in items:
        text = (
            item["name"] + " " +
            item["description"] + " " +
            item["location"]
        ).lower()

        if keyword in text:
            print_item(item)
            found = True

    if not found:
        print("No matching items found.")
