from tkinter import *
from constants import BASE_URL, ADMIN_GROUP
from tkinter import messagebox
from student_lobby import StudentLobby
from admin_lobby import AdminLobby
import requests


class Registration:
    def __init__(self, root):
        self.root = root
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
        self.name = str(self.entryName.get())
        self.group = str(self.entryGroup.get())
        data = {"name": self.entryName.get(), "group": self.entryGroup.get()}

        try:
            response = requests.post(f'{BASE_URL}/sign_in', json=data)

            if response.status_code == 200:
                if self.group != ADMIN_GROUP:
                    StudentLobby(self.root, self.name, self.group)
                else:
                    AdminLobby(self.root)
                #self.root.withdraw()
                #self.root.destroy()
            else:
                error_details = response.json().get("detail", "Неизвестная ошибка")
                messagebox.showerror("Error", f"Status {response.status_code}: {error_details}")
        except Exception as e:
            messagebox.showerror("Error", e)
            print(e)

    def helpMessage(self):
        messagebox.showinfo("Help", "Its test for education")


def main():
    root = Tk()
    registration = Registration(root)
    root.mainloop()

if __name__ == '__main__':
    main()
