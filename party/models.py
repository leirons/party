from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from core.db import Base


class Party(Base):
    __tablename__ = "party"
    id = Column(Integer, primary_key=True, index=True)
    name_of_party = Column(String, index=True)
    longitude = Column(Integer, index=True)
    latitude = Column(Integer, index=True)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)
    number_of_peoples_want_visit = Column(Integer, default=0)
    number_of_peoples_thinking = Column(Integer, default=0)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates='party')
    party = relationship("PartyParcipants",back_populates="parcipants")


class PartyParcipants(Base):
    __tablename__ = "party_parcipants"
    id = Column(Integer,index=True,primary_key=True)
    party_id = Column(Integer,ForeignKey("party.id"))
    party_owner = relationship("Party",back_populates="party_parcipants")