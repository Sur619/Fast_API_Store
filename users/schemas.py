import uuid

from pydantic import EmailStr, BaseModel


class ShowUser(BaseModel):
    # user_id: uuid.UUID
    name: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: bool = True
