from pydantic import BaseModel
from datetime import date

class ApartmentBase(BaseModel):
    owner: str
    street: str | None = None
    n_of_house: int | None = None
    n_of_apartment: int | None = None

class ApartmentCreate(ApartmentBase):
    pass

class Apartment(ApartmentBase):
    id: int
    class Config:
        orm_mode = True

class ChoreTypeBase(BaseModel):
    name: str
    is_have_counter: bool
    cost_per_month: float

class ChoreTypeCreate(ChoreTypeBase):
    pass

class ChoreType(ChoreTypeBase):
    id: int
    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    chore_id: int
    apartment_id: int
    cost: float
    month_year: str
    date_of_deposit: date

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    class Config:
        orm_mode = True
