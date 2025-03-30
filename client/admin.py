from tkinter import *

class Admin:
    def __init__(self, root):
        self.root = root
        self.windowSetup()
        self.windowSettings()

    def windowSetup(self):
        self.createTestBtn = Button(self.root, width=6, text="Create Test", command=self.createTest)
        self.startExamBtn = Button(self.root, width=6, text="Start Exam", command=self.startExam)
        self.createTestBtn.pack()
        self.startExamBtn.pack()

    def windowSettings(self):
        self.root.geometry("300x200")
        self.root.title("Admin")
    def createTest(self):
        pass
    def startExam(self):
        pass



# root = Tk()
# admin = Admin(root)
# root.mainloop()