from .. import models,schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from ..bcrypt import hashpassword


def all_users(db:Session):
    user=db.query(models.User).all() #all retuns only list if data avaialable or not
    return user

def user_filter(id,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f"user {id} not found")
    return user

def user_create(request:schemas.User,db:Session):
    hashed_password=hashpassword(request.password)
    user=models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user