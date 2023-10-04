from models.database_setup import create_session, engine, Base
from models.plant_model import Plant
from sqlalchemy.exc import IntegrityError

#Create DB tables if they don't exist yet
Base.metadata.create_all(engine)

session = create_session()

#Creating an array of plants to add to the DB
plants = [
    Plant(
        name="Aloe Vera",
        image_path="/static/plant_images/aloe_vera.jpg",
        soil_moisture="monthly",
        light_preference="direct",
        temperature_preference="warm",
        fertilizer_recommendation="Every 6 weeks"
    ),
    Plant(
        name="Snake Plant",
        image_path="/static/plant_images/snake_plant.jpg",
        soil_moisture="bi-weekly",
        light_preference="low",
        temperature_preference="warm",
        fertilizer_recommendation="Every 2 months"
    ),
    Plant(
        name="Spider Plant",
        image_path="/static/plant_images/spider_plant.jpg",
        soil_moisture="weekly",
        light_preference="indirect",
        temperature_preference="moderate",
        fertilizer_recommendation="Monthly"
    ),
    Plant(
        name="Lavender",
        image_path="/static/plant_images/lavender.jpg",
        soil_moisture="weekly",
        light_preference="direct",
        temperature_preference="warm",
        fertilizer_recommendation="Every 2 months"
    ),
    Plant(
        name="Rosemary",
        image_path="/static/plant_images/rosemary.jpg",
        soil_moisture="weekly",
        light_preference="direct",
        temperature_preference="moderate",
        fertilizer_recommendation="Every month"
    ),
    Plant(
        name="Pothos",
        image_path="/static/plant_images/pothos.jpg",
        soil_moisture="bi-weekly",
        light_preference="low",
        temperature_preference="moderate",
        fertilizer_recommendation="Every 2 months"
    ),
    Plant(
        name="Basil",
        image_path="/static/plant_images/basil.jpg",
        soil_moisture="bi-weekly",
        light_preference="direct",
        temperature_preference="warm",
        fertilizer_recommendation="Every month"
    ),
    Plant(
        name="Mint",
        image_path="/static/plant_images/mint.jpg",
        soil_moisture="bi-weekly",
        light_preference="indirect",
        temperature_preference="moderate",
        fertilizer_recommendation="Every 6 weeks"
    ),
    Plant(
        name="Peace Lily",
        image_path="/static/plant_images/peace_lily.jpg",
        soil_moisture="weekly",
        light_preference="low",
        temperature_preference="moderate",
        fertilizer_recommendation="Every 6 weeks"
    ),
    Plant(
        name="Orchid",
        image_path="/static/plant_images/orchid.jpg",
        soil_moisture="weekly",
        light_preference="indirect",
        temperature_preference="warm",
        fertilizer_recommendation="Every 3 weeks"
    ),
]

try:
    #Add plants to the DB
    for plant in plants:
        session.add(plant)

    #Commit the session
    session.commit()

except IntegrityError:
    session.rollback()
    print("Plants are already in the DB. Skipping insertion.")