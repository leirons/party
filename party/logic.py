from sqlalchemy.orm import Session
from party import models
from datetime import datetime


def get_parties(db: Session):
    return db.query(models.Party).all()


def create_party(party_name: str, longitude: int, latitude: int, user_id: int, db: Session, date: datetime):
    db_party = models.Party(name_of_party=party_name, longitude=longitude, latitude=latitude, owner_id=user_id,
                            data_to_visit=date)
    db.add(db_party)
    db.commit()
    db.refresh(db_party)
    return db_party


def delete_party(party_name: str, db: Session):
    try:
        db.query(models.Party).where(models.Party.name_of_party == party_name).delete()
        db.commit()
    except Exception as e:
        return False
    return True
