from pydantic import BaseModel
from typing import Optional

class Emp(BaseModel):
    
    emp_name :str
    emp_phone:Optional[int]=None
    emp_age:Optional[int]=None

class Show_emp(BaseModel):
    emp_name:str
    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str

class Show_user(BaseModel):
    name:str
    email:str
    class Config():
       orm_mode=True
class Authenication(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:Optional[str]=None