from sqlalchemy import Column, Integer, String, Boolean, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Apartment(Base):
    __tablename__ = "apartment"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String(100), nullable=False)
    street = Column(String(100))
    n_of_house = Column(Integer)
    n_of_apartment = Column(Integer)

    payments = relationship("Payment", back_populates="apartment")

class ChoreType(Base):
    __tablename__ = "chore_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    is_have_counter = Column(Boolean, nullable=False)
    cost_per_month = Column(Numeric(10, 2))

    payments = relationship("Payment", back_populates="chore")

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True)
    chore_id = Column(Integer, ForeignKey("chore_type.id", ondelete="CASCADE"))
    apartment_id = Column(Integer, ForeignKey("apartment.id", ondelete="CASCADE"))
    cost = Column(Numeric(15, 2))
    month_year = Column(String(100))
    date_of_deposit = Column(Date, nullable=False)

    chore = relationship("ChoreType", back_populates="payments")
    apartment = relationship("Apartment", back_populates="payments")
