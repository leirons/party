from pydantic import BaseModel,validator,ValidationError
from .validation import validate_email,if_have_symbols


class UserBase(BaseModel):
    email: str

    @validator("email")
    def validate_email(cls, email):
        if validate_email(email):
            return email
        return ValidationError("Email does not correct")


class UserCreate(UserBase):
    password: str
    login: str

    @validator("login")
    def validate_login(cls, login):
        if not if_have_symbols(login):
            if len(login) > 30:
                return ValidationError("Login should not have more then 30 symbols ")
            return login
        return ValidationError("Login has symbols")


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    password: str
    login:str

    @validator("login")
    def validate_login(cls, login):
        if not if_have_symbols(login):
            if len(login) > 30:
                return ValidationError("Login should not have more then 30 symbols ")
            return login
        return ValidationError("Login has symbols")

    class Config:
        orm_mode = True


class ChangeUserPassword(BaseModel):
    password: str
    new_password:str

    class Config:
        orm_mode = True
