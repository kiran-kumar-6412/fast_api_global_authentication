from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import jwt_token

Oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str=Depends(Oauth2_schema)):
    credintial_exception=HTTPException(status.HTTP_404_NOT_FOUND,
                                       "Could not validate Credintials")
    return jwt_token.verify_token(token,credintial_exception)