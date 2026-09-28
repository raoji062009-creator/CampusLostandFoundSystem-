from data_manager import USERS_FILE, load_data, save_data


def register_user():
    users = load_data(USERS_FILE)

    print("\n===== Register =====")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == "" or password == "":
        print("Username and password cannot be empty.")
        return

    for user in users:
        if user["username"] == username:
            print("Username already exists.")
            return

    users.append({
        "username": username,
        "password": password
    })

    save_data(USERS_FILE, users)
    print("Registration successful.")


def login():
    users = load_data(USERS_FILE)

    print("\n===== Login =====")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return username

    print("Wrong username or password.")
    return None
