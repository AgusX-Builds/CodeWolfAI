import tkinter as tk
from tkinter import messagebox

from save_manager import save_user
from achievements import check_achievements


def open_lesson1(user):

    window = tk.Toplevel()
    window.title("🐺 Lesson 1 - Variables")
    window.geometry("700x550")
    window.configure(bg="#202124")

    title = tk.Label(
        window,
        text="🐺 Lesson 1: Variables",
        font=("Arial", 22, "bold"),
        bg="#202124",
        fg="white"
    )
    title.pack(pady=20)

    lesson = """
Luna says:

Welcome to your first Python lesson!

A variable is like a box.

You can put information inside it and
give the box a name.

Example:

name = "Alex"

Now the variable called 'name'
stores the word Alex.

To display it:

print(name)

Output:

Alex
"""

    tk.Label(
        window,
        text=lesson,
        justify="left",
        font=("Arial", 14),
        bg="#202124",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        window,
        text="Question:\nWhich is a variable name?",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack(pady=15)

    def answer(correct):

        if correct:

            user["xp"] += 10
            user["coins"] += 5

            save_user(user)
            check_achievements(user)

            messagebox.showinfo(
                "Great Job!",
                "🐺 Correct!\n\n⭐ +10 XP\n🪙 +5 Coins"
            )

        else:

            messagebox.showinfo(
                "Luna",
                "Not quite!\n\nA variable is the name that stores information.\n\nExample:\nage = 13"
            )

        window.destroy()

    tk.Button(
        window,
        text="A) age",
        width=25,
        command=lambda: answer(True)
    ).pack(pady=5)

    tk.Button(
        window,
        text="B) print",
        width=25,
        command=lambda: answer(False)
    ).pack(pady=5)

    tk.Button(
        window,
        text="C) for",
        width=25,
        command=lambda: answer(False)
    ).pack(pady=5)
