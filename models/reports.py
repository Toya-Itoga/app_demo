from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base



class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(String, ForeignKey("lots.lot_id"), nullable=False)
    date = Column(DateTime, server_default=func.now(), nullable=False)
    plant_condition = Column(Integer, nullable=True)
    pest_and_disease_situation = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)
    image_path = Column(String, nullable=True)

    lot = relationship("Lots", back_populates="reports")