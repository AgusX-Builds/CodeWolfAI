import tkinter as tk
from quiz import open_quiz


def open_dashboard(user):

    window = tk.Toplevel()
    window.title("🐺 CodeWolf AI Dashboard")
    window.geometry("700x500")
    window.configure(bg="#202124")

    tk.Label(
        window,
        text=f"🐺 Welcome, {user['username']}!",
        font=("Arial", 24, "bold"),
        bg="#202124",
        fg="white"
    ).pack(pady=20)

    tk.Label(
        window,
        text=f"🏅 Rank: {user['rank']}",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack()

    tk.Label(
        window,
        text=f"⭐ XP: {user['xp']}",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack()

    tk.Label(
        window,
        text=f"🪙 Coins: {user['coins']}",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack()

    tk.Label(
        window,
        text=f"🔥 Streak: {user['streak']} Days",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack()

    tk.Label(
        window,
        text=f"🌍 World: {user['current_world']}",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack()

    tk.Label(
        window,
        text=f"📚 Lesson: {user['current_lesson']}",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack(pady=(0, 15))

    tk.Button(
        window,
        text="📚 Continue Learning",
        width=30,
        height=2
    ).pack(pady=5)

    tk.Button(
        window,
        text="🧠 Python Placement Quiz",
        width=30,
        height=2,
        command=lambda: open_quiz(user)
    ).pack(pady=5)

    tk.Button(
        window,
        text="🤖 AI Tutor (Coming Soon)",
        width=30,
        height=2
    ).pack(pady=5)

    tk.Button(
        window,
        text="⚙️ Settings",
        width=30,
        height=2
    ).pack(pady=5)

    tk.Button(
        window,
        text="🚪 Logout",
        width=30,
        height=2,
        command=window.destroy
    ).pack(pady=20)
