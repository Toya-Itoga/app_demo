from fastapi import APIRouter, Request, Form, Query, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import get_db
from services.reports_service import create_report_service
from schemas.schema import ReportCreate
from utils.datetime import today_iso



router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/create_report_form/{lot_id}")
def create_report_form_show(request: Request, lot_id: str):
    date = today_iso()
    return templates.TemplateResponse(
        "create_report_form.html",
        {
            "request": request,
            "lot_id": lot_id,
            "date": date,
        }
    )


@router.post("/create_report/{lot_id}")
def create_report(
    lot_id: str,
    date: str = Query(...),
    plant_status: int = Form(),
    pests_and_diseases_status: int = Form(),
    comment: str = Form(),
    # image_path: str = Form(),
    db: Session = Depends(get_db),
):
    report_data = ReportCreate(
        lot_id=lot_id,
        date=date,
        plant_status=plant_status,
        pests_and_diseases_status=pests_and_diseases_status,
        comment=comment,
        # image_path=image_path,
    )

    create_report_service(db, report_data)
    return RedirectResponse(url="/api/lots/get_all", status_code=303)