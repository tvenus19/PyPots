from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base

class Pot(Base):
    __tablename__ = "pots"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(String(50), default='EMPTY')

    #Defines the relationship with Plant model
    plant_id = Column(Integer, ForeignKey('plants.id'))
    plant = relationship('Plant', back_populates='pots')

    #Defines the relationship with SensorData model
    sensor_data = relationship('SensorData', back_populates='pot', foreign_keys='SensorData.pot_id')

    def __init__(self, name, location, status='EMPTY'):
        self.name = name
        self.location = location
        self.status = status