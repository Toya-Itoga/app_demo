from fastapi import FastAPI
from routers import reports_router
from routers import lots_router
from database import Base, engine
# from models.lots import Lots
# from models.reports import Reports



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(lots_router.router, prefix="/api/lots", tags=["Lots"])
app.include_router(reports_router.router, prefix="/api/reports", tags=["Reports"])