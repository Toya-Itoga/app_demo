from sqlalchemy.orm import Session
from typing import List
from repositories.reports_repositories import create_report_to_db
from schemas.schema import ReportCreate



def create_report_service(db: Session, report_data: ReportCreate):
    """
    新規日報を日報テーブルに追加するサービス関数
    """
    return create_report_to_db(db, report_data)