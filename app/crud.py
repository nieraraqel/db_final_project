from sqlalchemy.orm import Session
from . import models, schemas

# Apartments
def create_apartment(db: Session, apt: schemas.ApartmentCreate):
    db_apt = models.Apartment(**apt.dict())
    db.add(db_apt)
    db.commit()
    db.refresh(db_apt)
    return db_apt

def get_apartment(db: Session, apartment_id: int):
    return db.query(models.Apartment).filter(models.Apartment.id == apartment_id).first()

def get_apartments(db: Session):
    return db.query(models.Apartment).all()

def update_apartment(db: Session, apartment_id: int, apt_data: schemas.ApartmentCreate):
    apt = get_apartment(db, apartment_id)
    for key, value in apt_data.dict().items():
        setattr(apt, key, value)
    db.commit()
    db.refresh(apt)
    return apt

def delete_apartment(db: Session, apartment_id: int):
    apt = get_apartment(db, apartment_id)
    db.delete(apt)
    db.commit()
    return apt
