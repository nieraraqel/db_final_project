from fastapi import FastAPI
from .routers import apartment #, chore_type, payment

app = FastAPI()

app.include_router(apartment.router)
# app.include_router(chore_type.router)
# app.include_router(payment.router)
