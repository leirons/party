from typing import Optional, List

from fastapi import Depends, FastAPI, HTTPException


from user import schemes, logic, models
from core.db import SessionLocal, engine
from user.logic import *

from core.auth import AuthHandler

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
auth_handler = AuthHandler()



# TODO - Добавить токены к каждому endpoint

def get_db() -> SessionLocal:
    """
    Get db to create session
    :return Session:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemes.User)
def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
    """
    Function create user
    :param user:
    :param db:
    :return:
    """
    db_user = logic.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = auth_handler.get_passwords_hash(user.password)
    return logic.create_user(db=db, user=user,password=hashed_password)


@app.get("/user/{user_id}", response_model=schemes.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Function get user by id
    :param user_id:
    :param db:
    :return:
    """
    db_user = logic.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User does not exists")
    return db_user

@app.post("/users/login")
def login(user:schemes.UserToken,db:Session = Depends(get_db)):
    """
    Generate token for user
    :param user:
    :return token:
    """
    user_old = logic.get_user_by_login(db,user.login)

    if not user_old.email == user.login:
        return HTTPException(status_code=400,detail="Does not correct login")
    if auth_handler.verify_password(user.password,user_old.hash_password):
        token = auth_handler.encode_token(user_old.login,age=18)
        return {"token":token}



@app.get("/users/", response_model=List[schemes.User])
def get_all_user(skip:int = 0,limit:int = 100,db=Depends(get_db)):
    """
    Function gets all user from db
    :param db - Session of our database
    """
    db_user = logic.get_users(db,skip=skip,limit=limit)
    if not db_user:
        return HTTPException(status_code=404,detail="Users does not exists")
    return db_user



@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
   return {
       "username": username['sub'],
       "age": username["age"]
           }
