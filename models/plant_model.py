from sqlalchemy import Column, Integer, String, Enum
from .base import Base
from sqlalchemy.orm import relationship

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image_path = Column(String(255), nullable=False)
    soil_moisture = Column(Enum('daily', 'weekly', 'monthly'), nullable=False)
    light_preference = Column(Enum('daily', 'weekly', 'monthly'), nullable=False)
    temperature_preference = Column(Enum('warm', 'cold'), nullable=False)
    fertilizer_recommendation = Column(String(100), nullable=False)
    pots = relationship('Pot', back_populates='plant')

    def __init__(self, name, image_path, soil_moisture, light_preference, temperature_preference, fertilizer_recommendation=None):
        self.name = name
        self.image_path = image_path
        self.soil_moisture = soil_moisture
        self.light_preference = light_preference
        self.temperature_preference = temperature_preference
        self.fertilizer_recommendation = fertilizer_recommendation