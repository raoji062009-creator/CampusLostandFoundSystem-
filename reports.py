from data_manager import ITEMS_FILE, load_data


def show_report():
    items = load_data(ITEMS_FILE)

    lost = 0
    found = 0
    open_items = 0
    returned = 0

    for item in items:
        if item["type"] == "Lost":
            lost += 1
        elif item["type"] == "Found":
            found += 1

        if item["status"] == "Open":
            open_items += 1
        elif item["status"] == "Returned":
            returned += 1

    print("\n===== Campus Lost & Found Report =====")
    print("Total items:", len(items))
    print("Lost items:", lost)
    print("Found items:", found)
    print("Open items:", open_items)
    print("Returned items:", returned)
