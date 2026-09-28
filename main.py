from auth import login, register_user
from item_manager import add_item, view_items, update_item, delete_item, mark_as_found
from search import search_items
from reports import show_report
from data_manager import setup_files


def menu():
    print("\n===== CAMPUS LOST & FOUND SYSTEM =====")
    print("1. Add Lost/Found Item")
    print("2. View All Items")
    print("3. Search Items")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Mark Item as Found/Returned")
    print("7. Show Report")
    print("8. Logout")


def main():
    setup_files()

    print("===== Welcome =====")
    print("1. Login")
    print("2. Register")

    choice = input("Enter choice: ").strip()

    if choice == "2":
        register_user()

    username = login()

    if username is None:
        print("Login failed. Program ended.")
        return

    print("\nLogin successful. Welcome,", username)

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item(username)
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_items()
        elif choice == "4":
            update_item(username)
        elif choice == "5":
            delete_item(username)
        elif choice == "6":
            mark_as_found(username)
        elif choice == "7":
            show_report()
        elif choice == "8":
            print("Logged out. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
