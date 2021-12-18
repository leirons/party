from sqlalchemy import Boolean,Column,ForeignKey,INTEGER,Integer,String,Text
from sqlalchemy.orm import relationship
from core.db import Base
from party.models import Party


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    login  = Column(String,index=True)
    email = Column(String,index=True)
    country = Column(String,index=True)
    city = Column(String,index=True)
    hash_password = Column(String)

    parties = relationship(Party,back_populates="owner")




