from tkinter import *
from tkinter import messagebox, simpledialog, scrolledtext
from PIL import ImageTk, Image

root = Tk()
root.config()
root.title("Student Manager")
root.geometry('1366x768')
root.resizable(0,0)
root.iconphoto(False, ImageTk.PhotoImage(file="images3/student_logo.jpeg"))

def create_student(number, name, c1, c2, c3, exam):
    return {
        'number': number,
        'name': name,
        'course1': int(c1),
        'course2': int(c2),
        'course3': int(c3),
        'exam': int(exam)
    }

def calculate_totalcoursework(student):
    return student['course1'] + student['course2'] + student['course3']

def calculate_totaloverall(student):
    return calculate_totalcoursework(student) + student['exam']

def calculate_percentage(student):
    return round((calculate_totaloverall(student) / 160) * 100, 2)

def calculate_grade(student):
    percentage = calculate_percentage(student)
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def load_student_data():
    students = []
    try:
        with open("text_files2/studentMarks.txt", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(",")
                students.append(create_student(*parts))
    except FileNotFoundError:
        messagebox.showerror("Error", "text_files2/studentMarks.txt not found.")
        exit()
    return students

def save_student_data():
    with open("text_files2/studentMarks.txt", "w") as f:
        f.write(str(len(students)) + "\n")
        for student in students:
            f.write(f"{student['number']},{student['name']},{student['course1']},{student['course2']},{student['course3']},{student['exam']}\n")

students = load_student_data()

def format_student_output(student):
    return (f"Name: {student['name']}\n"
            f"Student Number: {student['number']}\n"
            f"Coursework Total: {calculate_totalcoursework(student)}/60\n"
            f"Exam Mark: {student['exam']}/100\n"
            f"Percentage: {calculate_percentage(student)}%\n"
            f"Grade: {calculate_grade(student)}\n"
            f"{'-'*40}\n")

def refresh_output():
    output.delete(1.0, END)

def view_totalstudents():
    refresh_output()
    total_percentage = 0
    for student in students:
        output.insert(END, format_student_output(student))
        total_percentage += calculate_percentage(student)
    class_avg = round(total_percentage / len(students), 2)
    output.insert(END, f"\nTotal Students: {len(students)}\n")
    output.insert(END, f"Class Average Percentage: {class_avg}%\n")

def view_student():
    search = simpledialog.askstring("Search", "Enter student name or number:")
    if not search:
        return
    refresh_output()
    for student in students:
        if search.lower() in student['name'].lower() or search == student['number']:
            output.insert(END, format_student_output(student))
            return
    messagebox.showinfo("Not Found", "No matching student found.")

def show_highestscore():
    best = max(students, key=lambda student: calculate_totaloverall(student))
    refresh_output()
    output.insert(END, "Highest Scoring Student:\n")
    output.insert(END, format_student_output(best))

def show_lowestscore():
    worst = min(students, key=lambda student: calculate_totaloverall(student))
    refresh_output()
    output.insert(END, "Lowest Scoring Student:\n")
    output.insert(END, format_student_output(worst))

def sort_students():
    choice = simpledialog.askstring("Sort", "Please type in 'asc' or 'desc':")
    if not choice:
        return
    if choice.lower() == "asc":
        students.sort(key=lambda student: calculate_totaloverall(student))
    elif choice.lower() == "desc":
        students.sort(key=lambda student: calculate_totaloverall(student), reverse=True)
    else:
        messagebox.showerror("Error", "Invalid choice. Enter asc or desc.")
        return
    refresh_output()
    view_totalstudents()

def add_student():
    number = simpledialog.askstring("Add Student", "Enter student number:")
    name = simpledialog.askstring("Add Student", "Enter student name:")
    c1 = simpledialog.askinteger("Add Student", "Coursework mark 1 (0–20):")
    c2 = simpledialog.askinteger("Add Student", "Coursework mark 2 (0–20):")
    c3 = simpledialog.askinteger("Add Student", "Coursework mark 3 (0–20):")
    exam = simpledialog.askinteger("Add Student", "Exam mark (0–100):")
    if None in (number, name, c1, c2, c3, exam):
        return
    students.append(create_student(number, name, c1, c2, c3, exam))
    save_student_data()
    messagebox.showinfo("Success", "Student added successfully.")
    view_totalstudents()

def delete_student():
    search = simpledialog.askstring("Delete Student", "Enter student name or number:")
    if not search:
        return
    for student in students:
        if search.lower() in student['name'].lower() or search == student['number']:
            students.remove(student)
            save_student_data()
            messagebox.showinfo("Deleted", "Student record deleted.")
            view_totalstudents()
            return
    messagebox.showinfo("Not Found", "No matching student found.")

def update_student():
    search = simpledialog.askstring("Update Student", "Enter student name or number:")
    if not search:
        return
    for student in students:
        if search.lower() in student['name'].lower() or search == student['number']:
            field = simpledialog.askstring(
                "Update",
                "What do you want to update?\n"
                "name, number, c1, c2, c3, exam"
            )
            if field == "name":
                student['name'] = simpledialog.askstring("Update", "Enter new name:")
            elif field == "number":
                student['number'] = simpledialog.askstring("Update", "Enter new student number:")
            elif field == "c1":
                student['course1'] = simpledialog.askinteger("Update", "Enter new coursework mark 1:")
            elif field == "c2":
                student['course2'] = simpledialog.askinteger("Update", "Enter new coursework mark 2:")
            elif field == "c3":
                student['course3'] = simpledialog.askinteger("Update", "Enter new coursework mark 3:")
            elif field == "exam":
                student['exam'] = simpledialog.askinteger("Update", "Enter new exam mark:")
            else:
                messagebox.showerror("Error", "Invalid field.")
                return
            save_student_data()
            messagebox.showinfo("Success", "Student record updated.")
            view_totalstudents()
            return
    messagebox.showinfo("Not Found", "No matching student found.")

bg = PhotoImage(file="images3/manager_bg.png")
main_frame = Label(root, image=bg)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

title = Label(root, text="Student Manager", font=("Helvetica", 50), fg="white", bg="#572f2f")
title.place(x=430, y=20)

btn1 = Button(root, text="View All Students", command=view_totalstudents, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn1.place(x=60, y=190)
btn2 = Button(root, text="View Student", command=view_student, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn2.place(x=60, y=250)
btn3 = Button(root, text="Highest Score", command=show_highestscore, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn3.place(x=60, y=310)
btn4 = Button(root, text="Lowest Score", command=show_lowestscore, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn4.place(x=60, y=370)
btn5 = Button(root, text="Sort Records", command=sort_students, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn5.place(x=60, y=430)
btn6 = Button(root, text="Add Student", command=add_student, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn6.place(x=60, y=490)
btn7 = Button(root, text="Delete Student", command=delete_student, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn7.place(x=60, y=550)
btn8 = Button(root, text="Update Student", command=update_student, width=15, font=("Helvetica", 18), borderwidth=0, fg="white", bg="#ab9685")
btn8.place(x=60, y=610)

menu_bar = Menu(root)
root.config(menu=menu_bar)

output = scrolledtext.ScrolledText(root, width=115, height=33)
output.place(x=370, y=180)

root.mainloop()