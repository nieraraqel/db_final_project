from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/apartment", tags=["Apartment"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Apartment)
def create_apartment(apt: schemas.ApartmentCreate, db: Session = Depends(get_db)):
    return crud.create_apartment(db, apt)

@router.get("/{apartment_id}", response_model=schemas.Apartment)
def read_apartment(apartment_id: int, db: Session = Depends(get_db)):
    return crud.get_apartment(db, apartment_id)

@router.get("/", response_model=list[schemas.Apartment])
def read_all(db: Session = Depends(get_db)):
    return crud.get_apartments(db)

@router.put("/{apartment_id}", response_model=schemas.Apartment)
def update(apartment_id: int, apt: schemas.ApartmentCreate, db: Session = Depends(get_db)):
    return crud.update_apartment(db, apartment_id, apt)

@router.delete("/{apartment_id}")
def delete(apartment_id: int, db: Session = Depends(get_db)):
    return crud.delete_apartment(db, apartment_id)
