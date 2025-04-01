from contextlib import asynccontextmanager
from fastapi import FastAPI
from server.database.database import delete_tables, create_tables
from server.routers.student_router import router as student_router
from server.routers.admin_router import router as admin_router
from server.routers.ws_router import router as ws_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base is clean up")
    await create_tables()
    print("Base is ready")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)
app.include_router(student_router)
app.include_router(admin_router)
app.include_router(ws_router)  
