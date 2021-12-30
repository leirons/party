from pydantic import BaseModel
from datetime import datetime


class PartyShow(BaseModel):
    name_of_party: str
    longitude: int
    latitude: int
    likes: str
    dislikes: str
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
