from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from PIL import ImageTk, Image
import random
root = Tk()
root.config()
root.title("Math Quiz")
root.geometry('1280x720')
root.resizable(0,0)
root.iconphoto(False, ImageTk.PhotoImage(file="images/m_logo.jpg"))

def switch_to_frame(frame):
    frame.tkraise()

class MathQuiz:
    def __init__(self, root):
        self.score = 0
        self.question_counter = 0
        self.current_answer = None
        self.difficulty = None
        
    def generate_question(self, difficulty):
        if difficulty == "easy":
            num_range = (1, 9)
        elif difficulty == "moderate":
            num_range = (10, 99)
        else:
            num_range = (1000, 9999)
        
        num1 = random.randint(*num_range)
        num2 = random.randint(*num_range)
        operation = random.choice(['+', '-'])
        
        if operation == '+':
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2
            
        return num1, operation, num2, correct_answer

    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.question_counter = 0
        self.next_question()

    def next_question(self):
        if self.question_counter < 10:
            self.question_counter += 1
            num1, operation, num2, correct_answer = self.generate_question(self.difficulty)
  
            question = f"{num1} {operation} {num2} ="
            self.current_answer = correct_answer
            
            self.display_question(question)
        else:
            self.show_results()

    def display_question(self, question):
        for widget in self.frame5.winfo_children():
            widget.destroy()
        
        question_label = Label(self.frame5, text=question, font=("Helvetica", 40), fg="black", bg="#f9f9f9")
        question_label.place(x=520, y=200)
        
        self.answer_entry = Entry(self.frame5, font=("Helvetica", 30), bd=5, relief=SOLID)
        self.answer_entry.place(x=520, y=300)
        
        submit_button = Button(self.frame5, text="Submit", font=("Helvetica", 20), bg="#d3d3d3", command=self.check_answer)
        submit_button.place(x=520, y=400)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        
        if user_answer == str(self.current_answer):
            self.score += 10
            self.next_question()
        else:
            retry_button = Button(self.frame5, text="Retry", font=("Helvetica", 20), bg="#f5f5f5", command=self.retry_question)
            retry_button.place(x=520, y=450)

    def retry_question(self):
        user_answer = self.answer_entry.get()
        
        if user_answer == str(self.current_answer):
            self.score += 5
            self.next_question()
        else:
            self.show_results()
        
    def show_results(self):
        for widget in self.frame8.winfo_children():
            widget.destroy()
        
        results_label = Label(self.frame8, text=f"Your Score: {self.score}", font=("Helvetica", 40), fg="black", bg="#f9f9f9")
        results_label.place(x=520, y=200)
        
        back_button = Button(self.frame8, text="Back to Menu", font=("Helvetica", 20), bg="#d3d3d3", command=lambda: self.switch_to_frame(self.frame2))
        back_button.place(x=520, y=300)

    def switch_to_frame(self, frame):
        frame.tkraise()

frame1 = Frame(root)
bg = PhotoImage(file="images/mathquiz_title.png")
main_label = Label(frame1, image=bg)
main_label.place(x=0, y=0, relwidth=1, relheight=1)
title = Label(frame1, text="Math Quiz", font=("Helvetica", 80), fg="black", bg="white")
title.place(x=390, y=260)
click_tostart = Label(frame1, text="Click Here to Start", font=("Helvetica", 20), fg="black", bg="#d2b071")
click_tostart.place(x=600, y=500)
btn_img= Image.open("images/start_button.png")
resized_btn= btn_img.resize((120,120))
new_image= ImageTk.PhotoImage(resized_btn)
start_button = Button(frame1, image=new_image, borderwidth=0, highlightthickness=0, relief=FLAT, border=0, command=lambda: switch_to_frame(frame2))
start_button.place(x=391, y=458)
frame1.place(width=1280,height=720)

frame2 = Frame(root)
bg_2 = PhotoImage(file="images/menu_page.png")
menu_frm = Label(frame2, image=bg_2)
menu_frm.place(x=0, y=0, relwidth=1, relheight=1)
menu_title = Label(frame2, text="Menu Page", font=("Helvetica", 50), fg="black", bg="#f5f3f5")
menu_title.place(x=470, y=160)
bckhm_btn = Button(frame2, text="Back to Home", font=("Helvetica", 25), borderwidth=0, bg="#f5f3f5", command=lambda: switch_to_frame(frame1))
bckhm_btn.place(x=530, y=298)
nstrct_btn = Button(frame2, text="Instructions", font=("Helvetica", 25), borderwidth=0, bg="#f5f3f5", command=lambda: switch_to_frame(frame3))
nstrct_btn.place(x=540, y=401)
bckhm_btn = Button(frame2, text="Start Quiz", font=("Helvetica", 25), borderwidth=0, bg="#f5f3f5", command=lambda: switch_to_frame(frame4))
bckhm_btn.place(x=550, y=503)
frame2.place(width=1280,height=720)

frame3 = Frame(root)
bg_3 = PhotoImage(file="images/instructions_page.png")
instructions_frm = Label(frame3, image=bg_3)
instructions_frm.place(x=0, y=0, relwidth=1, relheight=1)
instructions_title = Label(frame3, text="Instructions", font=("Helvetica", 45), fg="black", bg="#dfdfdf")
instructions_title.place(x=70, y=173)
instrct1 = Label(frame3, text="1. Select one out of the three \nlevels provided in this quiz: \neasy, moderate, and advanced.", font=("Helvetica", 18), fg="black", bg="#ffffff")
instrct1.place(x=450, y=150)
instrct2 = Label(frame3, text="2. For each level, there \nare 10 questions that you \nhave to answer correctly. \nThese questions will revolve around \naddition and subtraction.", font=("Helvetica", 18), fg="black", bg="#ffffff")
instrct2.place(x=810, y=300)
instrct3 = Label(frame3, text="3. You have multiple attempts \nto answer each question correctly. \nThe final score will be shown once \nyou finish the quiz.", font=("Helvetica", 18), fg="black", bg="#ffffff")
instrct3.place(x=430, y=450)
back_btn = Button(frame3, text="Back to Menu Page", font=("Helvetica", 19), borderwidth=0, bg="#fadfb5", command=lambda: switch_to_frame(frame2))
back_btn.place(x=91, y=470)
strtquiz_btn = Button(frame3, text="Start Quiz", font=("Helvetica", 19), borderwidth=0, bg="#fadfb5", command=lambda: switch_to_frame(frame4))
strtquiz_btn.place(x=142, y=540)
frame3.place(width=1280, height=720)

frame4 = Frame(root)
quiz = MathQuiz(root)
bg_4 = PhotoImage(file="images/difficulty_page.png")
difficulty_frm = Label(frame4, image=bg_4)
difficulty_frm.place(x=0, y=0, relwidth=1, relheight=1)
difficulty_title = Label(frame4, text="Difficulty", font=("Helvetica", 45), fg="black", bg="#e6e1d2")
difficulty_title.place(x=680, y=120)
select_instruct = Label(frame4, text="Please select one.", font=("Helvetica", 25), fg="black", bg="#f6f6f6")
select_instruct.place(x=110, y=173)
back_btn = Button(frame4, text="Back to Menu Page", font=("Helvetica", 19), borderwidth=0, bg="#fadfb5", command=lambda: quiz.start_quiz("easy"))
back_btn.place(x=91, y=490)
easy_link = Button(frame4, text="Easy", font=("Helvetica", 25), borderwidth=0, bg="#ffffff", command=lambda: switch_to_frame(frame5))
easy_link.place(x=520, y=330)
intermediate_link = Button(frame4, text="Intermediate", font=("Helvetica", 25), borderwidth=0, bg="#ffffff", command=lambda: quiz.start_quiz("moderate"))
intermediate_link.place(x=890, y=335)
advanced_link = Button(frame4, text="Advanced", font=("Helvetica", 25), borderwidth=0, bg="#ffffff", command=lambda: quiz.start_quiz("advanced"))
advanced_link.place(x=690, y=540)
frame4.place(width=1280, height=720)

frame5 = Frame(root)
bg_5 = PhotoImage(file="images/quiz_page.png")
quiz_frm = Label(frame5, image=bg_5)
quiz_frm.place(x=0, y=0, relwidth=1, relheight=1)
frame5.place(width=1280, height=720)

frame6 = Frame(root)
bg_6 = PhotoImage(file="images/quiz_page.png")
quiz_frm2 = Label(frame6, image=bg_6)
quiz_frm2.place(x=0, y=0, relwidth=1, relheight=1)
frame6.place(width=1280, height=720)

frame7 = Frame(root)
bg_7 = PhotoImage(file="images/quiz_page.png")
quiz_frm3 = Label(frame7, image=bg_7)
quiz_frm3.place(x=0, y=0, relwidth=1, relheight=1)
frame7.place(width=1280, height=720)

frame8 = Frame(root)
frame8.place(width=1280, height=720)

switch_to_frame(frame1)

root.mainloop()