from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    temperate = Column(Float, nullable=True)
    soil_moisture = Column(Float, nullable=True)
    light_level = Column(Float, nullable=True)
    ph_value = Column(Float, nullable=True)
    salinity = Column(Float, nullable=True)
    #Foreign key
    pot_id = Column(Integer, ForeignKey('pots.id'), nullable=False)
    pot = relationship('Pot', back_populates='sensor_data')

    def __init__(self, pot_id, temperature=None, soil_moisture=None, light_level=None, ph_value=None, salinity=None):
        self.pot_id = pot_id
        self.temperate = temperature
        self.soil_moisture = soil_moisture
        self.light_level = light_level
        self.ph_value = ph_value
        self.salinity = salinity