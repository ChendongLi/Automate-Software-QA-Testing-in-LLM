from fastapi import FastAPI
from app.routes import hello

app = FastAPI(title="Sample FastAPI App")

app.include_router(hello.router)