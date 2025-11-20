from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()
root.config()
root.title("Joke-Telling Assistant")
root.geometry('600x800')
root.resizable(0,0)
root.iconphoto(False, ImageTk.PhotoImage(file="images2/a_logo.jpeg"))

class JokeApp:
    def __init__(self, master):
        self.master = master
        master.title("Joke-Telling Assistant")

        self.jokes = self.load_jokes("text_files/randomJokes.txt")

        self.setup_label = Label(master, text="", font=("Arial", 14), wraplength=400, bg="#d7d9e4")
        self.setup_label.place(x=45, y=200)

        self.punchline_label = Label(master, text="", font=("Arial", 14, "italic"), wraplength=400, bg="#f9f5ed")
        self.punchline_label.place(x=115, y=330)

        self.tell_button = Button(master, text="Alexa tell me a Joke",
                                     command=self.show_setup, width=0, font=("Helvetica", 20), borderwidth=0, bg="white")
        self.tell_button.place(x=170, y=540)

        self.punchline_button = Button(master, text="Show Punchline",
                                          command=self.show_punchline, width=0, state="disabled", font=("Helvetica", 20), borderwidth=0, bg="white")
        self.punchline_button.place(x=190, y=630)

        self.next_button = Button(master, text="Next Joke",
                                     command=self.show_setup, width=0, state="disabled", font=("Helvetica", 20), borderwidth=0, bg="white")
        self.next_button.place(x=230, y=720)

        self.quit_button = Button(master, text="< Quit", command=master.quit, width=0, font=("Helvetica", 15), borderwidth=0, bg="#fafafa")
        self.quit_button.place(x=10, y=20)

        self.current_joke = None

    def load_jokes(self, filepath):
        jokes = []
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    if "?" in line:
                        setup, punchline = line.strip().split("?", 1)
                        jokes.append((setup + "?", punchline))
        except FileNotFoundError:
            jokes = [("Error: randomJokes.txt not found!", "Please add the file to the resources folder.")]
        return jokes

    def show_setup(self):
        self.current_joke = random.choice(self.jokes)
        setup, _ = self.current_joke

        self.setup_label.config(text=setup)
        self.punchline_label.config(text="")
        self.punchline_button.config(state="normal")
        self.next_button.config(state="normal")

    def show_punchline(self):
        if self.current_joke:
            _, punchline = self.current_joke
            self.punchline_label.config(text=punchline)

bg = PhotoImage(file="images2/background.png")
main_frame = Label(root, image=bg)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

alexa_title = Label(text="Alexa", font=("Helvetica", 30), bg="#fafafa")
alexa_title.place(x=250, y=14)

app = JokeApp(root)

root.mainloop()