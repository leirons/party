from sqlalchemy import Boolean,Column,ForeignKey,INTEGER,Integer,String
from sqlalchemy.orm import relationship
from core.db import Base
from party.models import Party,PartyParcipants


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    login  = Column(String,index=True)
    email = Column(String,index=True)
    country = Column(String,index=True)
    city = Column(String,index=True)
    hash_password = Column(String)
    number_of_creatied_parties = Column(Integer,default=0)

    party = relationship(Party,back_populates="owner")
    party_participants = relationship(PartyParcipants,back_populates='party_owner')




