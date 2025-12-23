from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/payments", tags=["Payment"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Payment)
def create(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db, payment)

@router.get("/{payment_id}", response_model=schemas.Payment)
def read(payment_id: int, db: Session = Depends(get_db)):
    return crud.get_payment(db, payment_id)

@router.get("/", response_model=list[schemas.Payment])
def read_all(db: Session = Depends(get_db)):
    return crud.get_payments(db)

@router.put("/{payment_id}", response_model=schemas.Payment)
def update(payment_id: int, payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return crud.update_payment(db, payment_id, payment)

@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
    return crud.delete_payment(db, payment_id)
