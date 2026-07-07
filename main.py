import tkinter as tk
from create_account import open_create_account
from login import open_login


class CodeWolfAI:

    def __init__(self, root):

        self.root = root
        self.root.title("🐺 CodeWolf AI")
        self.root.geometry("700x500")
        self.root.configure(bg="#202124")

        title = tk.Label(
            root,
            text="🐺 CodeWolf AI",
            font=("Arial", 28, "bold"),
            bg="#202124",
            fg="white"
        )

        title.pack(pady=20)

        subtitle = tk.Label(
            root,
            text="Learn. Build. Conquer.",
            font=("Arial", 14),
            bg="#202124",
            fg="lightgray"
        )

        subtitle.pack(pady=10)

        tk.Button(
            root,
            text="🔐 Login",
            width=25,
            height=2,
            command=open_login
        ).pack(pady=10)

        tk.Button(
            root,
            text="👤 Create Account",
            width=25,
            height=2,
            command=open_create_account
        ).pack(pady=10)

        tk.Button(
            root,
            text="❌ Exit",
            width=25,
            height=2,
            command=root.destroy
        ).pack(pady=10)


root = tk.Tk()
app = CodeWolfAI(root)
root.mainloop()
