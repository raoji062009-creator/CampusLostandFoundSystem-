import json
import os

DATA_FOLDER = "data"
USERS_FILE = os.path.join(DATA_FOLDER, "users.json")
ITEMS_FILE = os.path.join(DATA_FOLDER, "items.json")


def setup_files():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(USERS_FILE):
        save_data(USERS_FILE, [])

    if not os.path.exists(ITEMS_FILE):
        save_data(ITEMS_FILE, [])


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
