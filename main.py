from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import reports_router
from routers import lots_router
from database import Base, engine
# from models.lots import Lots
# from models.reports import Reports



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(lots_router.router, prefix="/api/lots", tags=["Lots"])
app.include_router(reports_router.router, prefix="/api/reports", tags=["Reports"])