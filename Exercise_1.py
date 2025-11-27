from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from PIL import ImageTk, Image
from random import randint, choice
root = Tk()
root.config()
root.title("Math Quiz")
root.geometry('1280x720')
root.resizable(0,0)
root.iconphoto(False, ImageTk.PhotoImage(file="images/m_logo.jpg"))

difficulty = ""
score = 0
questions = 0
question_count = 0
current_question = None

def switch_to_frame(frame):
    frame.tkraise()

def quiz_start(difficulty_level):
    global difficulty, score, questions, question_count
    difficulty = difficulty_level
    score = 0
    questions = 0
    question_count = 0
    switch_to_frame(frame5)
    next_question()

def random_int(difficulty_level):
    if difficulty_level == "easy":
        return randint(1,9)
    elif difficulty_level == "moderate":
        return randint(10, 99) 
    elif difficulty_level == "advanced":
        return randint(100, 999) 

def decide_operation():
    return choice(["+", "-"])

def next_question():
    global question_count, current_question
    if question_count >= 10:
        display_results()
        return
    num1 = random_int(difficulty)
    num2 = random_int(difficulty)
    operation = decide_operation()
    current_question = (num1, num2, operation)
    question_text = f"{num1} {operation} {num2} = ?"
    display_problem(question_text)
    question_count += 1

def display_problem(question_text):
    clear_screen()
    q_label = Label(frame5, text=question_text, font=("Helvetica", 30), bg="white")
    q_label.place(x=545, y=200)
    answr_entry = Entry(frame5, font=("Helvetica", 20))
    answr_entry.place(x=480, y=400)
    submit_bttn = Button(frame5, text="Submit", width=0, font=("Helvetica", 18), borderwidth=0, fg="black", bg="white", command=lambda: check_answer(answr_entry))
    submit_bttn.place(x=580, y=450)

def check_answer(answr_entry):
    correct_answer = calculate_answer(current_question)
    user_answer = answr_entry.get()
    if user_answer.strip().lstrip('-').isdigit():
        user_answer = int(user_answer.strip())
        if user_answer == correct_answer:
            global score
            score += 10
            next_question()
        else:
            messagebox.showinfo("Incorrect", f"First attempt incorrect. Try again.")
            answr_entry.delete(0, END)
            answr_entry.focus()
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def calculate_answer(question):
    num1, num2, operation = question
    if operation == '+':
        return num1 + num2
    else:
        return num1 - num2

def clear_screen():
    for widget in frame5.winfo_children():
        if widget != quiz_frm:
            widget.destroy()

def display_results():
    clear_screen()
    result_text = f"Your Score: {score} / 100"
    grade = get_grade(score)
    result_text += f"\nYour Grade: {grade}"
    label = Label(frame5, text=result_text, font=("Helvetica", 30), bg="white")
    label.place(x=450, y=200)
    play_again_btn = Button(frame5, text="Play Again", width=0, font=("Helvetica", 18), borderwidth=0, fg="black", bg="white", command=lambda: switch_to_frame(frame1))
    play_again_btn.place(x=560, y=450)

def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def display_menu():
    switch_to_frame(frame2)

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
start_quiz_btn = Button(frame2, text="Start Quiz", font=("Helvetica", 25), borderwidth=0, bg="#f5f3f5", command=lambda: switch_to_frame(frame4))
start_quiz_btn.place(x=550, y=503)
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
bg_4 = PhotoImage(file="images/difficulty_page.png")
difficulty_frm = Label(frame4, image=bg_4)
difficulty_frm.place(x=0, y=0, relwidth=1, relheight=1)
difficulty_title = Label(frame4, text="Difficulty", font=("Helvetica", 45), fg="black", bg="#e6e1d2")
difficulty_title.place(x=680, y=120)
select_instruct = Label(frame4, text="Please select one.", font=("Helvetica", 25), fg="black", bg="#f6f6f6")
select_instruct.place(x=110, y=173)
back_btn = Button(frame4, text="Back to Menu Page", font=("Helvetica", 19), borderwidth=0, bg="#fadfb5", command=lambda: switch_to_frame(frame2))
back_btn.place(x=91, y=490)
easy_link = Button(frame4, text="Easy", font=("Helvetica", 25), borderwidth=0, bg="#ffffff", command=lambda: quiz_start('easy'))
easy_link.place(x=520, y=330)
intermediate_link = Button(frame4, text="Intermediate", font=("Helvetica", 25), borderwidth=0, bg="#ffffff", command=lambda: quiz_start('moderate'))
intermediate_link.place(x=890, y=335)
advanced_link = Button(frame4, text="Advanced", font=("Helvetica", 25), borderwidth=0, bg="#ffffff", command=lambda: quiz_start('advanced'))
advanced_link.place(x=690, y=540)
frame4.place(width=1280, height=720)

frame5 = Frame(root)
bg_5 = PhotoImage(file="images/quiz_page.png")
quiz_frm = Label(frame5, image=bg_5)
quiz_frm.place(x=0, y=0, relwidth=1, relheight=1)
frame5.place(width=1280, height=720)

switch_to_frame(frame1)

root.mainloop()