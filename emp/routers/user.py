from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models,database
from sqlalchemy.orm import Session

from ..crud import user

route=APIRouter(
    
    tags=["Admin"]
)
get_db=database.get_db

@route.get("/allusers",response_model=list[schemas.Show_user])
def allusers(db:Session=Depends(get_db)):
    return user.all_users(db)

@route.get("/user/{id}",response_model=schemas.Show_user)
def filter_user(id,db:Session=Depends(get_db)):
    return user.user_filter(id,db,)

@route.post("/user",response_model=schemas.Show_user)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    # hashed_password=pass_contx.hash(request.password)
   return user.user_create(request,db)