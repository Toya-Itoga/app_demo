from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session

from database import get_db
from schemas.schema import LotsResponse, LotCreate
from services.lots_service import (
    get_all_lots_service,
    create_lot_service
)



router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/get_all")
def get_all_lots(request: Request, db: Session = Depends(get_db)):
    """
    ロット一覧画面を表示するAPIエンドポイント
    """
    lots = get_all_lots_service(db)
    return templates.TemplateResponse(
        "lots_show.html",
        {
            "request": request,
            "lots": lots,
        }
    )


@router.post("/create_lot")
def create_lot(
    lot_id: str = Form(...),
    farm: str = Form(...),
    house: str = Form(...),
    crops: Optional[str] = Form(None),
    grown_counts: Optional[int] = Form(None),
    created_at: Optional[datetime] = Form(None),
    db: Session = Depends(get_db)
):
    """
    DBに新規ロットを追加するAPIエンドポイント
    """

    lot_data = LotCreate(
        lot_id=lot_id,
        farm=farm,
        house=house,
        crops=crops,
        grown_counts=grown_counts,
        created_at=created_at,
    )

    create_lot_service(db, lot_data)

    return RedirectResponse("", status_code=303)