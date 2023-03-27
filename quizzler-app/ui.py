THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0, )
        self.question = self.canvas.create_text(150, 125, text="test", font=("arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.true_check)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.false_check)
        self.false_button.grid(row=2, column=1)
        self.update_score()
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check(self):
        user_answer = "True"
        self.feedback(self.quiz.check_answer(user_answer))
        self.update_score()

    def false_check(self):
        user_answer = "False"
        self.feedback(self.quiz.check_answer(user_answer))
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

