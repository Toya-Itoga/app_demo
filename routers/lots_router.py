from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from datetime import date
from sqlalchemy.orm import Session

from database import get_db
from schemas.schema import LotsResponse, LotCreate
from services.lots_service import (
    get_all_lots_service,
    create_lot_service
)



router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/get_all", name="all_lots")
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


@router.get("/add-form")
def lot_add_form(reuqest: Request):
    return templates.TemplateResponse(
        "partials/lot_modal.html",
        {
            "request": reuqest,
            "mode": "create",
            "lot": None,
        }
    )


# @router.get("/edit-form/{lot_id}")
# def lot_edit_form(request: Request, lot_id: str):
#     lot = 


@router.post("/create_lot")
def create_lot(
    lot_id: str = Form(...),
    farm: str = Form(...),
    house: str = Form(...),
    crops: Optional[str] = Form(None),
    grown_counts: Optional[int] = Form(None),
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
    )

    create_lot_service(db, lot_data)

    return RedirectResponse("", status_code=303)