from sqlalchemy import Column, Integer, String, Date, text
from sqlalchemy.orm import relationship
from database import Base



class Lots(Base):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True, index=True)
    lot_id = Column(String, nullable=False, index=True)
    farm = Column(String, nullable=False)
    house = Column(String, nullable=False)
    crops = Column(String, nullable=True)
    plant_counts = Column(Integer, nullable=True)
    grown_counts = Column(Integer, nullable=True)
    created_at = Column(Date, nullable=False, server_default=text("CURRENT_DATE"),)

    reports = relationship("Reports", back_populates="lot")