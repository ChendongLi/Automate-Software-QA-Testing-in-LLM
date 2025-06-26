from fastapi import APIRouter
from app.models.hello import HelloResponse

router = APIRouter()

@router.get("/hello", response_model=HelloResponse)
async def say_hello(name: str = "World"):
    # 👇 This line introduces a runtime error
    result = 1 / 0
    return HelloResponse(message=f"Hello, {name}!")