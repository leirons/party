from sqlalchemy.orm import Session
from party import models



#
# def get_parties()

def create_party(party_name:str,longitude:int,latitude:int,user_id:int,db:Session):
    db_party = models.Party(name_of_party=party_name,longitude=longitude,latitude=latitude,owner_id=user_id)
    db.add(db_party)
    db.commit()
    db.refresh(db_party)
    return db_party
