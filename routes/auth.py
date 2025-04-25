import uuid
import bcrypt
from fastapi import Depends, HTTPException

from database import get_db
from models.user import User
from fastapi import APIRouter
from sqlalchemy.orm import Session

from pydantic_schemas.user_create import CreateUser
from pydantic_schemas.user_login import UserLogin
router = APIRouter()


@router.post('/signup',status_code= 201)
def user_signup(user: CreateUser, db: Session = Depends(get_db)):
    # db.query(User).all()
     # it will return all the users present in the user table;
    user_db = db.query(User).filter(User.email == user.email).first() # all, search for all or return the first one.
    # the first User.email = db, user.email = requested through json;
    if  user_db:
        raise HTTPException(400, 'user exists with the same email')
    
    hash_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt(16))
    user_db = User(id = str(uuid.uuid4), password = hash_pw, email = user.email, name = user.name,)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db
@router.post('/login')
def user_login(user: UserLogin, db: Session = Depends(get_db)):
   user_db =  db.query(User).filter(User.email == user.email).first()
   if not user_db:
       raise HTTPException(400, "User with this email does not exist")
   
   is_matched = bcrypt.checkpw(user.password.encode(), user_db.password)
   if not is_matched:
       raise HTTPException(400, "Password not matched")
   return user_db
   
       
