from sqlalchemy import Boolean,Column,ForeignKey,Integer,String

from core.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    login  = Column(String,index=True)
    email = Column(String,index=True)
    hash_password = Column(String)

