import tkinter as tk
from tkinter import messagebox
import json
import os


def open_create_account():

    window = tk.Toplevel()
    window.title("🐺 Create Account")
    window.geometry("400x350")
    window.resizable(False, False)

    tk.Label(window, text="Username").pack(pady=5)
    username_entry = tk.Entry(window, width=30)
    username_entry.pack()

    tk.Label(window, text="Password").pack(pady=5)
    password_entry = tk.Entry(window, show="*", width=30)
    password_entry.pack()

    def save_account():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please enter a username and password."
            )
            return

        filename = "data/users.json"

        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    users = json.load(file)
            except:
                users = []
        else:
            users = []

        for user in users:
            if user["username"] == username:
                messagebox.showerror(
                    "Error",
                    "That username already exists."
                )
                return

        new_user = {
            "username": username,
            "password": password,
            "xp": 0,
            "coins": 0,
            "rank": "Wolf Pup",
            "quiz_completed": False,
            "current_world": 1,
            "current_lesson": 1,
            "badges": [],
            "streak": 0
        }

        users.append(new_user)

        with open(filename, "w") as file:
            json.dump(users, file, indent=4)

        messagebox.showinfo(
            "Success",
            "🐺 Account created successfully!"
        )

        window.destroy()

    tk.Button(
        window,
        text="Create Account",
        width=20,
        command=save_account
    ).pack(pady=20)
