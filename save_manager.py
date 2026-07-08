import json
import os


USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def save_user(updated_user):

    users = load_users()

    for i, user in enumerate(users):

        if user["username"] == updated_user["username"]:

            users[i] = updated_user
            break

    save_users(users)
