from pydantic import BaseModel


class PartyShow(BaseModel):
    name_of_party:str
    longitude:int
    latitude:int
    owner_id:str
    likes:str
    dislikes:str


    class Config:
        orm_mode = True


class PartyCreate(BaseModel):
    name_of_party:str
    longitude:int
    latitude:int

    class Config:
        orm_mode = True



