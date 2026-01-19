from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from schemas.schema import LotsResponse, LotCreate
from services.lots_service import (
    get_all_lots_service,
    create_lot_service
)



router = APIRouter()
# templates = 


@router.get("/get_all", response_model=List[LotsResponse])
def get_all_lots(db: Session = Depends(get_db)):
    """
    ロット一覧を返すAPIエンドポイント
    """
    lots = get_all_lots_service(db)
    return lots


@router.post("/create_lot", response_model=LotCreate)
def create_lot(lot_data: LotCreate, db: Session = Depends(get_db)):
    """
    DBに新規ロットを追加するAPIエンドポイント
    """
    return create_lot_service(db, lot_data)