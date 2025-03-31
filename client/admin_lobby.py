from tkinter import *
import requests
from constants import BASE_URL

class AdminLobby:
    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.windowSetup()
        self.windowSettings()
        self.updateStats()


    def updateStats(self):
        try:
            response = requests.get(f"{BASE_URL}/admin/stats")
            data = response.json()
            text = f"Count of student: {data}"
            self.statsLabel.config(text=text)
        except Exception as e:
            print("Ошибка обновления:", e)
        
        self.window.after(5000, self.updateStats)

    def windowSetup(self):
        self.statsLabel = Label(self.window, text="Sats...")
        self.statsLabel.pack()
        self.createTestBtn = Button(self.window, width=6, text="Create Test", command=self.createTest)
        self.startExamBtn = Button(self.window, width=6, text="Start Exam", command=self.startExam)
        self.createTestBtn.pack()
        self.startExamBtn.pack()

    def windowSettings(self):
        self.window.geometry("300x200")
        self.window.title("Admin")
    
    def createTest(self):
        pass
    
    def startExam(self):
        pass
