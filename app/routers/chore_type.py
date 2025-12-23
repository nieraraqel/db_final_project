from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/chore-types", tags=["ChoreType"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ChoreType)
def create(chore: schemas.ChoreTypeCreate, db: Session = Depends(get_db)):
    return crud.create_chore_type(db, chore)

@router.get("/{chore_id}", response_model=schemas.ChoreType)
def read(chore_id: int, db: Session = Depends(get_db)):
    return crud.get_chore_type(db, chore_id)

@router.get("/", response_model=list[schemas.ChoreType])
def read_all(db: Session = Depends(get_db)):
    return crud.get_chore_types(db)

@router.put("/{chore_id}", response_model=schemas.ChoreType)
def update(chore_id: int, chore: schemas.ChoreTypeCreate, db: Session = Depends(get_db)):
    return crud.update_chore_type(db, chore_id, chore)

@router.delete("/{chore_id}")
def delete(chore_id: int, db: Session = Depends(get_db)):
    return crud.delete_chore_type(db, chore_id)
