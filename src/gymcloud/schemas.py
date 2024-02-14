from pydantic import BaseModel


class UsersBase(BaseModel):
    email: str
    
class UsersCreate(UsersBase):
    password: str
    username: str
    
class Users(UsersBase):
    id: int
    
    class Config:
        orm_mode = True