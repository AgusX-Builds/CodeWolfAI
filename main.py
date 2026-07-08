import tkinter as tk
from screens.login import open_login


class CodeWolfAI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("🐺 CodeWolf AI")
        self.root.geometry("900x600")
        self.root.configure(bg="#202124")

        tk.Label(
            self.root,
            text="🐺 CodeWolf AI",
            font=("Arial", 30, "bold"),
            bg="#202124",
            fg="white"
        ).pack(pady=40)

        tk.Label(
            self.root,
            text="Learn Python with Luna!",
            font=("Arial", 16),
            bg="#202124",
            fg="white"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="🚀 Start",
            font=("Arial", 16),
            width=20,
            height=2,
            command=open_login
        ).pack(pady=30)

        tk.Button(
            self.root,
            text="❌ Exit",
            font=("Arial", 16),
            width=20,
            height=2,
            command=self.root.destroy
        ).pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CodeWolfAI()
    app.run()
