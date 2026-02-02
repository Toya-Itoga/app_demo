from sqlalchemy.orm import Session
from models.lots import Lots
from typing import List
from schemas.schema import LotCreate, LotUpdate



def get_all_lots_from_db(db: Session) -> List[Lots]:
    """
    ロットテーブルから全件取得する関数
    """
    return db.query(Lots).all()


def get_lot_by_lot_id_from_db(db: Session, lot_id: str) -> List[Lots]:
    """
    指定されたロットIDの情報のみ取得する関数
    """
    return db.query(Lots).filter(Lots.lot_id == lot_id).first()


def create_lot_to_db(db: Session, lot_data: LotCreate):
    """
    新規ロットをロットテーブルに追加する関数
    """
    lot = Lots(
        lot_id=lot_data.lot_id,
        farm=lot_data.farm,
        house=lot_data.house,
        crops=lot_data.crops,
        plant_counts=lot_data.plant_counts,
        grown_counts=lot_data.plant_counts,
    )

    db.add(lot)
    db.commit()
    db.refresh(lot)

    return lot


def update_lot_to_db(db: Session, lot_id: str, update_data: LotUpdate):
    lot = db.query(Lots).filter(Lots.lot_id == lot_id).first()

    if not lot:
        return None
    
    lot.farm = update_data.farm
    lot.house = update_data.house
    lot.crops = update_data.crops
    lot.plant_counts = update_data.plant_counts
    lot.grown_counts = update_data.grown_counts

    db.commit()
    db.refresh(lot)
    return lot