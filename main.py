from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
async def getPage():
    return {"ok": True}
