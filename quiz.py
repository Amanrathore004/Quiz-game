import tkinter as tk
from tkinter import messagebox

# Questions and answers dictionary
questions = [
    {
        "question": 'Where in the computer is a variable such as "c" stored after the following Python line finishes?\n\nc = 123',
        "options": ["Central processing unit", "Main Memory", "Secondary Memory", "Input Devices"],
        "answer": "Main Memory",
    },
    {
        "question": "What will the following program print out?\n\nx = 43\nx = x + 1\nprint(x)",
        "options": ["43", "44", "x + 1", "Error because x = x + 1 is not possible mathematically"],
        "answer": "44",
    },
    {
        "question": "What will the following Python program print out?\n\ndef fred():\n    print('Zap')\n\ndef jane():\n    print('ABC')\n\njane()\nfred()\njane()",
        "options": ["Zap ABC jane fred jane", "Zap ABC Zap", "ABC Zap jane", "ABC Zap ABC"],
        "answer": "ABC Zap ABC",
    },
    {
        "question": "What is the output of the following program?\n\nprint(1)\nx = 2\nprint(x)",
        "options": ["4", "2", "5", "1"],
        "answer": "2",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.root.geometry("500x400")

        self.username = ""
        self.score = 0
        self.current_question = 0

        self.create_welcome_screen()

    def create_welcome_screen(self):
        """Creates the welcome screen where the user enters their name."""
        self.clear_screen()

        self.label = tk.Label(self.root, text="Enter your name:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Arial", 12), bg="lightgreen")
        self.start_button.pack(pady=20)

    def start_quiz(self):
        """Starts the quiz after getting the username."""
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showwarning("Warning", "Please enter your name to start the quiz!")
            return

        self.show_question()

    def show_question(self):
        """Displays the current question and answer choices."""
        self.clear_screen()

        question_data = questions[self.current_question]

        self.question_label = tk.Label(self.root, text=question_data["question"], font=("Arial", 12), wraplength=450, justify="left")
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")
        self.options_buttons = []

        for i, option in enumerate(question_data["options"]):
            rb = tk.Radiobutton(self.root, text=option, variable=self.options_var, value=option, font=("Arial", 10))
            rb.pack(anchor="w", padx=20)
            self.options_buttons.append(rb)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12), bg="lightblue")
        self.next_button.pack(pady=20)

    def next_question(self):
        """Checks the answer and moves to the next question."""
        selected_answer = self.options_var.get()

        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        if selected_answer == questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(questions):
            self.show_question()
        else:
            self.show_score()

    def show_score(self):
        """Displays the final score."""
        self.clear_screen()

        result_text = f"Quiz Completed!\n{self.username}, your final score: {self.score}/{len(questions)}"
        self.result_label = tk.Label(self.root, text=result_text, font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=30)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12), bg="red", fg="white")
        self.exit_button.pack(pady=20)

    def clear_screen(self):
        """Removes all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
