from fastapi import FastAPI
from schemas import Registration

app = FastAPI()

@app.post("/sign_in")
async def sign_in(data: Registration):
    return {"okey": True}

