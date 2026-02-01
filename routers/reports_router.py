from fastapi import APIRouter, Request, Form, Query, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from services.reports_service import (
    create_report_service,
    update_report_service,
    get_report_by_lot_id_service,
    get_report_by_lot_and_date_service,
)
from schemas.schema import ReportCreate, ReportUpdate
from utils.datetime import today_iso



router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/create_report_form/{lot_id}")
def create_report_form_show(request: Request, lot_id: str, db: Session = Depends(get_db)):
    date = today_iso()
    existing_report = get_report_by_lot_and_date_service(db, lot_id, date)
    return templates.TemplateResponse(
        "create_report_form.html",
        {
            "request": request,
            "lot_id": lot_id,
            "date": date,
            "existing_report": existing_report,
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


@router.post("/update_report/{lot_id}")
def update_report(
    lot_id: str,
    date: str = Query(None),
    plant_status: int = Form(...),
    pests_and_diseases_status: int = Form(...),
    comment: str = Form(...),
    db: Session = Depends(get_db),
):
    update_data = ReportUpdate(
        plant_status=plant_status,
        pests_and_diseases_status=pests_and_diseases_status,
        comment=comment,
    )

    update_report_service(db, lot_id, date, update_data)

    return RedirectResponse(url="/api/lots/get_all", status_code=303)


@router.get("/get_reports/{lot_id}")
def get_reports_by_id(
    request: Request,
    lot_id: str,
    date: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    all_reports = get_report_by_lot_id_service(db, lot_id, date)
    detail_report = all_reports["detail_report"]
    reports = all_reports["reports"]
    return templates.TemplateResponse(
        "reports_list.html",
        {
            "request": request,
            "detail_report": detail_report,
            "reports": reports,
        }
    )