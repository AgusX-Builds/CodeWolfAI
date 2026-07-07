import tkinter as tk
from tkinter import messagebox


questions = [
    {
        "question": "What does print('Hello') display?",
        "options": ["Error", "Hello", "Nothing"],
        "answer": "Hello"
    },
    {
        "question": "Which keyword creates a loop?",
        "options": ["print", "for", "input"],
        "answer": "for"
    },
    {
        "question": "What symbol is used for comments?",
        "options": ["//", "#", "*"],
        "answer": "#"
    },
    {
        "question": "What stores information?",
        "options": ["Variable", "Loop", "Function"],
        "answer": "Variable"
    },
    {
        "question": "Which function gets user input?",
        "options": ["input()", "print()", "len()"],
        "answer": "input()"
    }
]


def open_quiz(user):

    window = tk.Toplevel()
    window.title("🐺 Python Placement Quiz")
    window.geometry("700x500")

    score = 0
    current = 0

    question_label = tk.Label(
        window,
        font=("Arial", 18),
        wraplength=600
    )
    question_label.pack(pady=20)

    buttons = []

    def show_question():

        nonlocal current

        q = questions[current]

        question_label.config(
            text=f"Question {current+1}/{len(questions)}\n\n{q['question']}"
        )

        for b in buttons:
            b.destroy()

        buttons.clear()

        for option in q["options"]:

            btn = tk.Button(
                window,
                text=option,
                width=30,
                command=lambda o=option: check_answer(o)
            )

            btn.pack(pady=5)

            buttons.append(btn)

    def check_answer(choice):

        nonlocal current
        nonlocal score

        if choice == questions[current]["answer"]:
            score += 1

        current += 1

        if current >= len(questions):
            finish()
        else:
            show_question()

    def finish():

        if score <= 2:
            rank = "🐺 Wolf Pup"
        elif score <= 4:
            rank = "🐺 Scout"
        else:
            rank = "🐺 Hunter"

        messagebox.showinfo(
            "Quiz Complete",
            f"You scored {score}/{len(questions)}!\n\nYour starting rank is:\n{rank}"
        )

        window.destroy()

    show_question()
