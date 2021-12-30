from fastapi import APIRouter, Path, Depends, HTTPException, UploadFile, File

from typing import Optional, List

from user import schemes, logic, models
from core.db import SessionLocal, engine, get_db
from user.logic import *

from core.auth import AuthHandler

models.Base.metadata.create_all(bind=engine)
auth_handler = AuthHandler()

router = APIRouter()


# TODO - Добавить токены к каждому endpoint


@router.post("/users/", response_model=schemes.User, tags=['User'])
async def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
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
    return await logic.create_user(db=db, user=user, password=hashed_password)


@router.post("/users/change_password{password}",tags=["User"])
async def change_login(user_scheme:schemes.ChangeUserPassword,db: Session = Depends(get_db),
                 user=Depends(auth_handler.auth_wrapper)):

    user_ = await logic.get_user_by_id(user_id=user['sub'], db=db)

    if user['sub'] == user_.id:
        if auth_handler.verify_password(user_scheme.password,user_.hash_password):
            await logic.change_password(user_scheme.new_password, user, db)
            return {"Operation":"Success"}
        return HTTPException(status_code=401, detail="Password does not correct")
    return {"Operation": "Error"}

@router.get("/user/{user_id}", response_model=schemes.User, tags=["User"])
async def get_user(user_id: int = Path(..., title="Id of user"), db: Session = Depends(get_db)):
    """
    Function get user by id
    :param user_id:
    :param db:
    :return:user
    """
    db_user = await logic.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User does not exists")
    return db_user


@router.post("/users/login", tags=["User"])
async def login(user: schemes.UserToken, db: Session = Depends(get_db)):
    """
    Generate token for user
    :param user:
    :return token:
    """
    user_old = await logic.get_user_by_login(db, user.login)

    if not user_old.login == user.login:
        return HTTPException(status_code=400, detail="Does not correct login")
    if auth_handler.verify_password(user.password, user_old.hash_password):
        token = auth_handler.encode_token(user_old.id, age=18)  # TODO
        return {"token": token}


@router.get("/users/", response_model=List[schemes.User], tags=["User"])
async def get_all_user(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    """
    Function gets all user from db
    :param db - Session of our database
    """
    db_user = await     logic.get_users(db, skip=skip, limit=limit)
    if not db_user:
        return HTTPException(status_code=404, detail="Users does not exists")
    return db_user




