from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from party import schemes
from core.auth import AuthHandler
from core.db import get_db
from party import logic


router = APIRouter()
auth = AuthHandler()


@router.post(path="/party_create/{number_of_party}",status_code=201,tags=["Party"],response_model=schemes.PartyCreate)
def party_create(party:schemes.PartyCreate,user=Depends(auth.auth_wrapper),db:Session = Depends(get_db)):
    party =  logic.create_party(party_name=party.name_of_party,longitude=party.longitude,latitude=party.latitude,user_id=user['sub'],db=db)
    return party