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

# ChoreType 
def create_chore_type(db: Session, chore: schemas.ChoreTypeCreate):
    db_chore = models.ChoreType(**chore.dict())
    db.add(db_chore)
    db.commit()
    db.refresh(db_chore)
    return db_chore

def get_chore_type(db: Session, chore_id: int):
    return db.query(models.ChoreType).filter(models.ChoreType.id == chore_id).first()

def get_chore_types(db: Session):
    return db.query(models.ChoreType).all()

def update_chore_type(db: Session, chore_id: int, chore_data: schemas.ChoreTypeCreate):
    chore = get_chore_type(db, chore_id)
    for key, value in chore_data.dict().items():
        setattr(chore, key, value)
    db.commit()
    db.refresh(chore)
    return chore

def delete_chore_type(db: Session, chore_id: int):
    chore = get_chore_type(db, chore_id)
    db.delete(chore)
    db.commit()
    return chore

# Payment 
def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()

def get_payments(db: Session):
    return db.query(models.Payment).all()

def update_payment(db: Session, payment_id: int, payment_data: schemas.PaymentCreate):
    payment = get_payment(db, payment_id)
    for key, value in payment_data.dict().items():
        setattr(payment, key, value)
    db.commit()
    db.refresh(payment)
    return payment

def delete_payment(db: Session, payment_id: int):
    payment = get_payment(db, payment_id)
    db.delete(payment)
    db.commit()
    return payment
