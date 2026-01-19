from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base



class Lots(Base):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(String, nullable=False, index=True)
    farm = Column(String, nullable=False)
    house = Column(String, nullable=False)
    crops = Column(String, nullable=True)
    grown_counts = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    reports = relationship("Reports", back_populates="lot")