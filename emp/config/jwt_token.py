import jwt
from jwt.exceptions import InvalidTokenError
from datetime import timedelta,datetime,timezone
from ..repository import schemas



SECRETE_KEY="kiran@123"
ALGORITHM="HS256"
EXPRIRE_TIME_MINUTES=30

def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(EXPRIRE_TIME_MINUTES)
    to_encode.update({"exp":expire})
    jwt_token=jwt.encode(to_encode,SECRETE_KEY,algorithm=ALGORITHM)
    return jwt_token

def verify_token(token:str,exception_from_oath2):
    try:
        paylod=jwt.decode(token,SECRETE_KEY,algorithms=ALGORITHM)
        token_email:str=paylod.get("sub")
        if not token_email:
            raise exception_from_oath2
        token_data=schemas.TokenData(email=token_email)
    except InvalidTokenError:
        raise exception_from_oath2
        
