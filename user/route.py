from fastapi import APIRouter
from user.schemas import ShowUser, CreateUser

user_router = APIRouter()


@user_router.get("/")
async def root():
    return {"message": "Hello World"}


@user_router.post("/users")
async def users(user: CreateUser):
    return [

            {"name": user.name, "email": user.email}
    ]
