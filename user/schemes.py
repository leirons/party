from pydantic import BaseModel,validator,ValidationError
from .validation import validate_email,if_have_symbols

class UserBase(BaseModel):
    email: str

    @validator("email")
    def validate_email(cls, email):
        if validate_email(email):
            print(validate_email(email))
            return email
        return ValidationError("Email does not correct")


class UserCreate(UserBase):
    password: str
    login: str

    @validator("login")
    def validate_login(cls, login):
        if not if_have_symbols(login):
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
            return login
        return ValidationError("Login has symbols")

    class Config:
        orm_mode = True

