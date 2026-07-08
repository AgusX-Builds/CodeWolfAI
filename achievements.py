from tkinter import messagebox
from save_manager import save_user


def check_achievements(user):

    if "First Lesson" not in user["badges"] and user["xp"] >= 10:

        user["badges"].append("First Lesson")
        user["xp"] += 25
        user["coins"] += 10

        save_user(user)

        messagebox.showinfo(
            "🏆 Achievement Unlocked!",
            "🐺 First Lesson\n\n"
            "+25 XP\n"
            "+10 Coins"
        )

    if "100 XP Club" not in user["badges"] and user["xp"] >= 100:

        user["badges"].append("100 XP Club")
        user["coins"] += 50

        save_user(user)

        messagebox.showinfo(
            "🏆 Achievement Unlocked!",
            "⭐ 100 XP Club\n\n"
            "+50 Coins"
        )
