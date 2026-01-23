from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.reports import Reports
from typing import List
from schemas.schema import ReportCreate



def get_all_reports_from_db(db: Session) -> List[Reports]:
    """
    日報テーブルから全件取得する関数
    """
    return db.query(Reports).all()


def get_report_by_lot_id_from_db(db: Session, lot_id: str) -> List[Reports]:
    """
    特定のロットIDに紐づく日報を取得する関数
    """
    return (
        db.query(Reports)
        .filter(Reports.lot_id == lot_id)
        .order_by(desc(Reports.date))
        .all()
    )


def create_report_to_db(db: Session, report_data: ReportCreate):
    """
    新規日報を日報テーブルに追加する関数
    """
    report = Reports(
        lot_id=report_data.lot_id,
        date=report_data.date,
        plant_condition=report_data.plant_condition,
        pest_and_disease_situation=report_data.pest_and_disease_situation,
        comment=report_data.comment,
        image_path=report_data.image_path
    )

    db.add(report)
    db.commit()
    db.refresh()

    return report