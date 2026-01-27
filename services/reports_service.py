from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any

from repositories.reports_repositories import (
    create_report_to_db,
    get_report_by_lot_id_from_db
)
from schemas.schema import ReportCreate



def create_report_service(db: Session, report_data: ReportCreate):
    """
    新規日報を日報テーブルに追加するサービス関数
    """
    return create_report_to_db(db, report_data)


def get_report_by_lot_id_service(db: Session, lot_id: str, date_q: Optional[str] = None) -> Dict[str, Any]:
    """
    特定のロットIDに紐づく日報を取得するサービス関数
    """
    items = get_report_by_lot_id_from_db(db, lot_id)

    items_dict: List[Dict[str, Any]] = []
    for i in items:
        row = {
            "id": i.id,
            "lot_id": i.lot_id,
            "date": i.date,
            "plant_condition": i.plant_status,
            "pest_and_disease_situation": i.pests_and_diseases_status,
            "comment": i.comment,
            "image_path": i.image_path,
        }
        items_dict.append(row)

    target_index = 0
    if date_q:
        for index, item in enumerate(items_dict):
            if item.get("date") == date_q:
                target_index = index
                break

    # 詳細表示する日報
    detail_report = items_dict[target_index]

    # 簡易表示する日報
    reports: List[Dict[str, Any]] = []
    for index, item in enumerate(items_dict):
        if index == target_index:
            continue
        reports.append(item)

    return {
        "detail_report": detail_report,
        "reports": reports
    }