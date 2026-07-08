import tkinter as tk
from tkinter import messagebox
import io
import contextlib


def open_wolf_lab(user):

    window = tk.Toplevel()
    window.title("🐺 Wolf Lab")
    window.geometry("800x600")
    window.configure(bg="#202124")

    tk.Label(
        window,
        text="🐺 Wolf Lab",
        font=("Arial", 24, "bold"),
        bg="#202124",
        fg="white"
    ).pack(pady=10)

    tk.Label(
        window,
        text="Write Python code below and press Run!",
        bg="#202124",
        fg="white",
        font=("Arial", 12)
    ).pack()

    editor = tk.Text(
        window,
        height=15,
        width=80,
        font=("Courier New", 12)
    )

    editor.pack(pady=10)

    editor.insert(
        "1.0",
        'name = "Agustin"\nprint("Hello", name)'
    )

    output = tk.Text(
        window,
        height=10,
        width=80,
        bg="black",
        fg="lime",
        font=("Courier New", 11)
    )

    output.pack(pady=10)

    def run_code():

        code = editor.get("1.0", tk.END)

        output.delete("1.0", tk.END)

        try:

            text = io.StringIO()

            with contextlib.redirect_stdout(text):
                exec(code, {})

            output.insert(tk.END, text.getvalue())

        except Exception as e:

            output.insert(tk.END, f"❌ Error:\n\n{e}")

    tk.Button(
        window,
        text="▶ Run Code",
        width=20,
        height=2,
        command=run_code
    ).pack(pady=10)
