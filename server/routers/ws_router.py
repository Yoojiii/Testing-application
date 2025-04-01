from fastapi import APIRouter, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["websockets"])

students = set()
admin = None

@router.websocket("/ws/student")
async def student_endpoint(websocket: WebSocket):
    await websocket.accept()
    students.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            if data == "START_EXAM":
                print("Студент получил команду начать экзамен")
    except:
        students.remove(websocket)


@router.websocket("/ws/admin")
async def admin_endpoint(websocket: WebSocket):
    global admin
    await websocket.accept()
    admin = websocket
    try:
        while True:
            data = await websocket.receive_text()
            if data == "START_EXAM":
                for student in students:
                    await student.send_text("START_EXAM")
    except:
        admin = None

