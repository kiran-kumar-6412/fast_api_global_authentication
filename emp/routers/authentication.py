from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, jwt_token,schemas,models,bcrypt


router=APIRouter(
    tags=['Login']
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user_name=db.query(models.User).filter(models.User.email==request.username).first()
    if not user_name:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"Incorrect email")
    password=bcrypt.verify(request.password,user_name.password)
    if not password:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"Incorrect password")
    return {"Acess_token":jwt_token.create_token(data={"sub":user_name.email})}

