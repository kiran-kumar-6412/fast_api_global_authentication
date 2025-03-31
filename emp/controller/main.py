from fastapi import FastAPI

from ..repository import models
from ..repository import database
from ..repository.database import engine

from ..service import emp,user,authentication


app=FastAPI()
get_db=database.get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app.include_router(emp.router)
app.include_router(user.route)
app.include_router(authentication.router)


@app.get("/")
def home():
    return"hey"








