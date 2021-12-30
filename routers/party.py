from fastapi import APIRouter, Depends, Cookie, Header, Path, Body
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
async def party_create(party: schemes.PartyCreate, user=Depends(auth.auth_wrapper), db: Session = Depends(get_db)):
    party = await logic.create_party(party_name=party.name_of_party, longitude=party.longitude, latitude=party.latitude,
                               user_id=user['sub'], db=db, date=party.data_to_visit)
    return party


@router.post(path='/party_get_all', tags=["Party"], response_model=List[schemes.PartyShow])
async def party_all(db: Session = Depends(get_db)):
    return await logic.get_parties(db=db)


@router.post(path='/party_delete/{name_of_party}', tags=["Party"], status_code=201)
async def delete_party(party: schemes.PartyDelete, db: Session = Depends(get_db),user=Depends(auth.auth_wrapper)):
    if await logic.delete_party(party_name=party.name_of_party, db=db):
        return {"Operation": "Success"}
    return {"Operation": "Failed"}


@router.post('/party_join/{id_of_party}', tags=['Party'])
async def join_to_the_party(party_scheme: schemes.PartyParticipantsCreate, db: Session = Depends(get_db),
                            user=Depends(auth.auth_wrapper)):
    if await logic.join_to_the_party(id=party_scheme.party_id, db=db, owner_id=user['sub']):
        return {"Operation": "Success"}
    return {"Operation": "Failed"}
