from sqlalchemy.orm import Session

from . import models, schemes


async def get_user_by_name(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


async def get_user_by_id(db: Session, user_id: int):
    return  db.query(models.User).filter(models.User.id == user_id).first()


async def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


async def get_user_by_login(db: Session, login: str):
    return  db.query(models.User).filter(models.User.login == login).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


async def create_user(password: str, db: Session, user: schemes.UserCreate):
    db_user = models.User(email=user.email, hash_password=password, login=user.login)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def change_password(password: str, user: models.User, db: Session):
    from core.auth import AuthHandler
    handler = AuthHandler()
    hash_password = handler.get_passwords_hash(password)
    user = get_user_by_id(user_id=user['sub'],db=db)
    user.hash_password = hash_password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def get_all_users(db: Session):
    db_user = db.query(models.User).all()
    return db_user
