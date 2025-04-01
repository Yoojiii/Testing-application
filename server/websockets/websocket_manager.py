import asyncio
from threading import Thread
import websockets

class AdminWebsockets:
    def startExam(self):
        Thread(target=self.start_exam_async).start()

    def start_exam_async(self):
        asyncio.run(self.send_start_command())

    async def send_start_command(self):
        async with websockets.connect("ws://localhost:8000/ws/admin") as ws:
            await ws.send("START_EXAM")
            print("Exam started for all students")


class StudentWebsockets:
    def __init__(self, status_callback=None):
        self.callback = 0
        self.status_callback = status_callback

    def start_listen(self):
        Thread(target=self.listen_for_exam, daemon=True).start()

    def listen_for_exam(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.listen_async())

    async def listen_async(self):
        try:
            async with websockets.connect("ws://localhost:8000/ws/student") as ws:
                while True:
                    message = await ws.recv()
                    if message == "START_EXAM":
                        self.callback = 1
                        if self.status_callback:
                            self.status_callback(1)
                        break
        except Exception as e:
            print(f"WebSocket error: {e}")
            self.callback = -1
            if self.status_callback:
                self.status_callback(-1)