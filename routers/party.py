from fastapi import APIRouter,Depends,Cookie,Header,Path,Body
from sqlalchemy.orm import Session
from party import schemes
from core.auth import AuthHandler
from core.db import get_db
from party import logic
from typing import List
from user.logic import get_user_by_login


router = APIRouter()
auth = AuthHandler()


@router.post(path="/party_create/{number_of_party}", status_code=201, tags=["Party"],
             response_model=schemes.PartyCreate)
def party_create(party: schemes.PartyCreate, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db)):
    party = logic.create_party(party_name=party.name_of_party, longitude=party.longitude, latitude=party.latitude,
                               user_id=user['sub'], db=db, date=party.data_to_visit)
    return party


@router.post(path='/party_get_all', tags=["Party"], response_model=List[schemes.PartyShow])
def party_all(db: Session = Depends(get_db)):
    return logic.get_parties(db=db)


@router.post(path='/party_delete/{name_of_party}',tags=["Party"],status_code=201)
def delete_party(party:schemes.PartyDelete,db:Session = Depends(get_db)):
    if logic.delete_party(party_name=party.name_of_party,db=db):
        return True
    return False
