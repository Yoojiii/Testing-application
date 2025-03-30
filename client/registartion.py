from tkinter import *
from tkinter import messagebox
import requests
class Registration:
    def __init__(self, root, name="", group=""):
        self.root = root
        self.name = name
        self.group = group
        self.windowSetup()
    def windowSettings(self):
        self.root.geometry("300x200")
        self.root.title("Sign in")

    def windowSetup(self):
        self.windowSettings()
        labelName = Label(self.root, text="Name:")
        labelGroup = Label(self.root, text="Group:")
        self.entryName = Entry(self.root, width=25)
        self.entryGroup = Entry(self.root, width=25)
        self.btnSignIn = Button(self.root, text="Sign in",width=6, command=self.submit)
        self.btnHelp = Button(self.root, text="Help", width=6, command=self.helpMessage)
        labelName.pack()
        self.entryName.pack()
        labelGroup.pack()
        self.entryGroup.pack()
        self.btnSignIn.pack()
        self.btnHelp.pack()

    def submit(self):
        self.name = self.entryName.get()
        self.group = self.entryGroup.get()

        response = requests.post("http://127.0.0.1:8000/sign_in",
                                 json={"name": self.name, "group": self.group})

        if response.status_code == 200:
            print("Response from server:", response.json())
        else:
            print("Error:", response.status_code)

    def helpMessage(self):
        messagebox.showinfo("help", "Its test for education")


def main():
    root = Tk()
    registration = Registration(root)
    root.mainloop()

if __name__ == '__main__':
    main()
