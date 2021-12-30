from pydantic import BaseModel
from datetime import datetime


class PartyShow(BaseModel):
    name_of_party: str
    longitude: int
    latitude: int
    likes: int
    dislikes: int
    owner_id:int

    class Config:
        orm_mode = True


class PartyCreate(BaseModel):
    name_of_party: str
    longitude: int
    latitude: int
    data_to_visit: datetime

    class Config:
        orm_mode = True


class PartyDelete(BaseModel):
    name_of_party: str

    class Config:
        orm_mode = True


class PartyParticipantsCreate(BaseModel):
    party_id: int
    class Config:
        orm_mode = True
