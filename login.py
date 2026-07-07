import tkinter as tk
from tkinter import messagebox
import json
import os

from dashboard import open_dashboard


def open_login():

    window = tk.Toplevel()
    window.title("🐺 Login")
    window.geometry("400x300")
    window.resizable(False, False)

    tk.Label(window, text="Username").pack(pady=5)
    username_entry = tk.Entry(window, width=30)
    username_entry.pack()

    tk.Label(window, text="Password").pack(pady=5)
    password_entry = tk.Entry(window, show="*", width=30)
    password_entry.pack()

    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        filename = "data/users.json"

        if not os.path.exists(filename):
            messagebox.showerror("Error", "No users found.")
            return

        with open(filename, "r") as file:
            try:
                users = json.load(file)
            except:
                users = []

        for user in users:
            if user["username"] == username and user["password"] == password:
                messagebox.showinfo(
                    "Success",
                    f"Welcome back, {username}!"
                )

                open_dashboard(username)
                window.destroy()
                return

        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )

    tk.Button(
        window,
        text="Login",
        command=login,
        width=20
    ).pack(pady=20)
