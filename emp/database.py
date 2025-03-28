from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "mysql+pymysql://root:kiran%40123@localhost/fastapi?charset=utf8mb4"

engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
