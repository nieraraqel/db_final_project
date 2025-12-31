from app.database import SessionLocal
from app.models import Apartment, Payment, ChoreType
from sqlalchemy.orm import joinedload
from sqlalchemy import func, select

session = SessionLocal()

# 1. SELECT ... WHERE
apartments_high_street = session.query(Apartment.owner).filter(
    Apartment.street == "High",
    Apartment.floor > 1
).all()

# 2. JOIN
payments_with_chore = session.query(Payment, ChoreType.cost_per_month).join(
    ChoreType, Payment.cost == ChoreType.cost_per_month
).all()

# 3. UPDATE
session.query(Apartment).filter(
    Apartment.id.in_(
        session.query(Payment.apartment_id).filter(Payment.cost < 10000)
    )
).update({Apartment.owner: "New Owner"}, synchronize_session="fetch")
session.commit()

# 4. GROUP BY
costs_grouped = session.query(
    ChoreType.id,
    func.sum(Payment.cost)
).join(Payment, Payment.cost == ChoreType.cost_per_month).group_by(ChoreType.id).all()

# 5. SELECT
sorted_apartments = session.query(Apartment).order_by(Apartment.owner).all()

session.close()
