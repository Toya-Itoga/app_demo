from pydantic import BaseModel, field_validator
from datetime import date



class LotsResponse(BaseModel):
    id: int
    lot_id: str
    farm: str
    house: str
    crops: str | None = None
    grown_counts: int = None
    created_at: date | None = None

    model_config = {"from_attributes": True}


class LotCreate(BaseModel):
    lot_id: str
    farm: str
    house: str
    crops: str | None = None
    grown_counts: int | None = None

    @field_validator("grown_counts", mode="before")
    def normalize_fullwidth_numbers(cls, v):
        if v is None:
            return None
        
        if isinstance(v, str):
            v = v.translate(str.maketrans(
                "0 1 2 3 4 5 6 7 8 9",
                "0123456789"
            ))
            return int(v)
        
        return v


class LotUpdate(BaseModel):
    farm: str
    house: str
    crops: str
    grown_counts: int | None = None


class ReportCreate(BaseModel):
    lot_id: str
    date: date
    plant_status: int
    pests_and_diseases_status: int
    comment: str | None = None
    image_path: str | None = None

    model_config = {"from_attributes": True}


class ReportUpdate(BaseModel):
    plant_status: int
    pests_and_diseases_status: int
    comment: str