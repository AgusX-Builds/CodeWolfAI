import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What does print('Hello') display?",
        "options": ["Error", "Hello", "Nothing"],
        "answer": "Hello",
        "explanation": "print() displays text on the screen."
    },
    {
        "question": "Which keyword creates a loop?",
        "options": ["print", "for", "input"],
        "answer": "for",
        "explanation": "A for loop repeats code."
    },
    {
        "question": "What symbol starts a comment in Python?",
        "options": ["//", "#", "*"],
        "answer": "#",
        "explanation": "Python uses # for comments."
    },
    {
        "question": "What stores information?",
        "options": ["Variable", "Loop", "Function"],
        "answer": "Variable",
        "explanation": "Variables store data."
    },
    {
        "question": "Which function asks the user for input?",
        "options": ["input()", "print()", "len()"],
        "answer": "input()",
        "explanation": "input() lets the user type something."
    },
    {
        "question": "Which function prints text?",
        "options": ["print()", "input()", "open()"],
        "answer": "print()",
        "explanation": "print() displays information."
    },
    {
        "question": "What is 5 + 3?",
        "options": ["8", "53", "2"],
        "answer": "8",
        "explanation": "Python can do math just like a calculator."
    },
    {
        "question": "Which symbol means 'equal to'?",
        "options": ["=", "==", "!="],
        "answer": "==",
        "explanation": "== compares two values."
    },
    {
        "question": "Which data type stores text?",
        "options": ["String", "Integer", "Boolean"],
        "answer": "String",
        "explanation": "Strings store letters and words."
    },
    {
        "question": "What does len() do?",
        "options": [
            "Counts how many items",
            "Prints text",
            "Creates a loop"
        ],
        "answer": "Counts how many items",
        "explanation": "len() returns the length of something."
    }
]


def open_quiz(user):

    window = tk.Toplevel()
    window.title("🐺 Python Placement Quiz")
    window.geometry("700x500")

    score = 0
    current = 0
    wrong_answers = []

    question_label = tk.Label(
        window,
        font=("Arial", 18),
        wraplength=600
    )
    question_label.pack(pady=20)

    buttons = []

    def show_question():

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

        nonlocal score
        nonlocal current

        if choice == questions[current]["answer"]:
            score += 1
        else:

            wrong_answers.append({

                "question": questions[current]["question"],
                "your_answer": choice,
                "correct_answer": questions[current]["answer"],
                "explanation": questions[current]["explanation"]

            })

        current += 1

        if current == len(questions):
            finish()
        else:
            show_question()

    def finish():

        if score <= 3:
            rank = "🐺 Wolf Pup"
        elif score <= 7:
            rank = "🐺 Scout"
        else:
            rank = "🐺 Hunter"

        report = f"🐺 Luna's Quiz Report\n\n"
        report += f"Score: {score}/{len(questions)}\n"
        report += f"Rank: {rank}\n\n"

        if wrong_answers:

            report += "Let's review what you missed:\n\n"

            for item in wrong_answers:

                report += f"❌ {item['question']}\n"
                report += f"Your answer: {item['your_answer']}\n"
                report += f"✅ Correct: {item['correct_answer']}\n"
                report += f"💡 Luna: {item['explanation']}\n\n"

        else:

            report += "🎉 Perfect Score!\n\n"
            report += "Luna says:\n"
            report += "Amazing job! You're ready for the next challenge!"

        messagebox.showinfo(
            "Quiz Results",
            report
        )

        window.destroy()

    show_question()
