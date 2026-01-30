from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from repositories.lots_repositories import (
    get_all_lots_from_db,
    create_lot_to_db,
    get_lot_by_lot_id_from_db,
    update_lot_to_db,
)
from models.lots import Lots
from schemas.schema import LotCreate




def get_all_lots_service(db: Session) -> List[Lots]:
    """
    ロットテーブルの一覧を取得して返すサービス関数
    """
    lots = get_all_lots_from_db(db)
    return lots


def get_lot_by_lot_id_service(db: Session, lot_id: str):
    """
    指定されたロットIDの情報のみ取得するサービス関数
    """
    return get_lot_by_lot_id_from_db(db, lot_id)



def create_lot_service(db: Session, lot_data: LotCreate) -> Lots:
    """
    新規ロットをロットテーブルに追加するサービス関数
    """
    lot = create_lot_to_db(db, lot_data)
    return lot


def update_lot_service(db: Session, lot_id: str, update_data: LotCreate):
    lot = get_lot_by_lot_id_from_db(db, lot_id)
    if not lot:
        raise HTTPException(status_code=404, detail="Lot not found")
    
    update_lot = update_lot_to_db(db, lot_id, update_data)

    return update_lot