from tkinter import *
from tkinter import messagebox
import requests

class Student:
    def __init__(self, root):
        self.root = root
        self.windowSettings()

    def windowSettings(self):
        self.root.geometry("300x200")
        self.root.title("Student")

# root = Tk()
# sudent = Student(root)
# root.mainloop()