import tkinter as tk


def open_dashboard(username):

    window = tk.Toplevel()
    window.title("🐺 CodeWolf Dashboard")
    window.geometry("700x500")
    window.configure(bg="#202124")

    title = tk.Label(
        window,
        text=f"🐺 Welcome, {username}!",
        font=("Arial", 24, "bold"),
        bg="#202124",
        fg="white"
    )
    title.pack(pady=20)

    tk.Label(
        window,
        text="Rank: 🐺 Wolf Pup",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack(pady=5)

    tk.Label(
        window,
        text="XP: 0 / 100",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack(pady=5)

    tk.Label(
        window,
        text="Coins: 0",
        font=("Arial", 16),
        bg="#202124",
        fg="white"
    ).pack(pady=5)

    tk.Button(
        window,
        text="📚 Learn Python",
        width=25,
        height=2
    ).pack(pady=10)

    tk.Button(
        window,
        text="🧠 Python Quiz",
        width=25,
        height=2
    ).pack(pady=10)

    tk.Button(
        window,
        text="🤖 AI Tutor",
        width=25,
        height=2
    ).pack(pady=10)

    tk.Button(
        window,
        text="🚪 Logout",
        width=25,
        height=2,
        command=window.destroy
    ).pack(pady=20)
