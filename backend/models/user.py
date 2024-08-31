# models/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    CLIENT = "client"
    LAWYER = "lawyer"
    MEDIATOR = "mediator"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole

    
class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class UserResponse(UserBase):
    id: str
