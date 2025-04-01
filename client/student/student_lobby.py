import sys
from pathlib import Path
import threading
from tkinter import Toplevel, Label

root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))

from server.websockets.websocket_manager import StudentWebsockets
from student.student_qa import StudentQA

class StudentLobby:
    def __init__(self, parent, name, group):
        self.window = Toplevel(parent)
        self.name = name
        self.group = group
        self.setup_ui()
        self.start_listening()

    def setup_ui(self):
        self.window.geometry("400x300")
        self.window.title("Lobby")
        self.status_label = Label(self.window, text="Waiting for exam to start...")
        self.status_label.pack()

    def start_listening(self):
        self.student_ws = StudentWebsockets()
        self.student_ws.start_listen()
        self.check_status()

    def check_status(self):
        if self.student_ws.callback == 1:
            self.on_exam_start()
        elif self.student_ws.callback == -1:
            self.status_label.config(text="Connection error!")
        else:
            self.window.after(100, self.check_status)

    def on_exam_start(self):
        self.status_label.config(text="Exam started!")
        StudentQA(self.window)