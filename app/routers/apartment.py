from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud, models

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
def read_all(
    page: int = Query(1, ge=1), 
    size: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    skip = (page - 1) * size
    apartments = db.query(models.Apartment).offset(skip).limit(size).all()
    return apartments

@router.put("/{apartment_id}", response_model=schemas.Apartment)
def update(apartment_id: int, apt: schemas.ApartmentCreate, db: Session = Depends(get_db)):
    return crud.update_apartment(db, apartment_id, apt)

@router.delete("/{apartment_id}")
def delete(apartment_id: int, db: Session = Depends(get_db)):
    return crud.delete_apartment(db, apartment_id)
