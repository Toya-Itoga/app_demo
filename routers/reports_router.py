from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.reports_service import create_report_service



router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/create_report_form/{lot_id}")
def create_report_form_show(request: Request, lot_id: str):
    return templates.TemplateResponse(
        "create_report_form.html",
        {
            "request": request,
            "lot_id": lot_id
        }
    )