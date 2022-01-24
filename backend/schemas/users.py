from typing import Optional
from xmlrpc.client import boolean
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password: str

class ShowUser(BaseModel):
    username : str
    email : EmailStr
    is_active : bool

    class Config():
        orm_mode = True