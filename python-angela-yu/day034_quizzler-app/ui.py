from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # ======
        # LAYOUT
        # ======

        # kita pakai grid layout (row, col)
        # 0,0     0,1
        # 1,0     1,1
        # 2,0     2,1

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Quiz", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        self.skor = Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR)
        self.skor.grid(row=0, column=1)
        
        ceklis_img = PhotoImage(file="day034_quizzler-app/images/true.png")
        self.ceklis = Button(image=ceklis_img, command=self.klik_ceklis, highlightthickness=0, bg=THEME_COLOR)
        self.ceklis.grid(row=2, column=0)

        silang_img = PhotoImage(file="day034_quizzler-app/images/false.png")
        self.silang = Button(image=silang_img, command=self.klik_silang, highlightthickness=0, bg=THEME_COLOR)
        self.silang.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.silang.config(state="active")
        self.ceklis.config(state="active")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.skor.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz selesai!")
            self.skor.config(text=f"Score: {self.quiz.score}")
            self.silang.config(state="disabled")
            self.ceklis.config(state="disabled")



    def klik_ceklis(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def klik_silang(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        self.silang.config(state="disabled")
        self.ceklis.config(state="disabled")
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg="green")
            # self.silang.config(state="active")
            # self.ceklis.config(state="active")
        else:
            self.canvas.config(bg="red")
            # self.silang.config(state="active")
            # self.ceklis.config(state="active")


