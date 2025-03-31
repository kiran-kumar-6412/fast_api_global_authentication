from passlib.context import CryptContext

pass_ctx=CryptContext(["bcrypt"],deprecated="auto")

def hashpassword(password):
    return pass_ctx.hash(password)

def verify(plain_password,Hashed_password):
    return pass_ctx.verify(plain_password,Hashed_password)