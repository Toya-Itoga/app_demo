from sqlalchemy.orm import Session
from typing import List
from repositories.lots_repositories import (
    get_all_lots_from_db,
    create_lot_to_db,
)
from models.lots import Lots
from schemas.schema import LotCreate




def get_all_lots_service(db: Session) -> List[Lots]:
    """
    ロットテーブルの一覧を取得して返すサービス関数
    """
    lots = get_all_lots_from_db(db)
    return lots


def create_lot_service(db: Session, lot_data: LotCreate) -> Lots:
    """
    新規ロットをロットテーブルに追加するサービス関数
    """
    lot = create_lot_to_db(db, lot_data)
    return lot