import datetime

from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from core.db import Base


class PartyParcipants(Base):
    __tablename__ = "party_owner"
    id = Column(Integer, index=True, primary_key=True)
    party_id = Column(Integer, ForeignKey("party.id"))
    party_parcipants = relationship("Party", back_populates="party")


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
    data_to_visit = Column(DateTime, default=datetime.datetime.now())

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates='party')

    party = relationship(PartyParcipants, back_populates="party_parcipants")
