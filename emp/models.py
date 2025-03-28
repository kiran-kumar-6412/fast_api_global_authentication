from .database import Base
from sqlalchemy import Column, Integer, String

class Emp(Base):
    __tablename__ = "emp"
    id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(100), nullable=False)
    emp_phone = Column(Integer, nullable=True)
    emp_age = Column(Integer, nullable=True)

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    email=Column(String(100))
    password=Column(String(255))
