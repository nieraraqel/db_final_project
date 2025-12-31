from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import apartment, chore_type, payment

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(apartment.router)
app.include_router(chore_type.router)
app.include_router(payment.router)

