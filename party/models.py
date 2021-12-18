from sqlalchemy import Column,String,ForeignKey,INTEGER

from core.db import Base


class Party(Base):
    __tablename__ = "party"
    id = Column(INTEGER,primary_key=True,index=True)
    name_of_party = Column(String,index=True)
    longitude = Column(INTEGER,index=True)
    width = Column(INTEGER,index=True)
    likes = Column(INTEGER)
    dislikes = Column(INTEGER)
