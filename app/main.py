from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user
from app.routers import auth

from app.routers import module

from app.routers import health


app = FastAPI(title="Core ERP - G0")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

app.include_router(module.router)

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"msg": "Core ERP rodando"}

