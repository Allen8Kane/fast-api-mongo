from src.routes.user import router as UserRouter
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

app.include_router(UserRouter, tags=["User"], prefix="/api/users")
