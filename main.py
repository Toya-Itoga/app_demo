from fastapi import FastAPI
from routers import lots_router
from database import engine
from models import product



product.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(lots_router.router, prefix="/lots", tags=["Lots"])