from tkinter import *
from tkinter import messagebox
from constants import BASE_URL


class StudentLobby:

    def __init__(self, parent, name, group):
        self.window = Toplevel(parent) 
        self.name = name
        self.group = group
        self.windowSettings()
        self.windowSetup()

    def windowSetup(self):
        Label(self.window, text="Waiting admin, exam will start soon!").pack()

    def windowSettings(self):
        self.window.title("Lobby")
        self.window.geometry("400x300")    