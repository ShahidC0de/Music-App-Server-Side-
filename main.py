
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
app = FastAPI()
DATABASE_URL = 'postgresql://postgres:shahid@localhost:5432/music_app'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False,autoflush=False, bind = engine)
db = SessionLocal()
class CreateUser(BaseModel):
    name:str
    email: str
    password:str
@app.post('/signup')
def user_signup(user: CreateUser):
    print(user.name)
    print(user.email)
    print(user.password)
