import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.true_image = tkinter.PhotoImage(file="images/true.png")
        self.false_image = tkinter.PhotoImage(file="images/false.png")

        self.score = tkinter.Label(text="Score: 0", bg=THEME_COLOR)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 100, font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280,
                                                text="Amazon acquired Twitch in August 2014 for $970 million dollars.")
        self.true_btn = tkinter.Button(image=self.true_image, bg=THEME_COLOR,
                                       command=self.true_pressed, highlightthickness=0)
        self.false_btn = tkinter.Button(image=self.false_image, bg=THEME_COLOR,
                                        command=self.false_pressed, highlightthickness=0)

        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=15)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text="You've completed the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
        self.score.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
