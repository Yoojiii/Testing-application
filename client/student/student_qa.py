from tkinter import *
from tkinter import messagebox
import requests

class StudentQA:
    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.windowSettings()

    def windowSettings(self):
        self.window.geometry("500x400")
        self.window.title("QA")

# root = Tk()
# sudent = Student(root)
# root.mainloop()