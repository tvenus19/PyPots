from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

Base = declarative_base()

class  User(Base):
    __tablename__ = 'users'

    id= Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

# Create an SQLite database
engine = create_engine('sqlite:///users.db')

# Create tables
Base.metadata.create_all(engine)

# Create a session
def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Function to initialize the DB and create a DB user if it doesn't exist
session = create_session()
existing_user = session.query(User).filter_by(username="admin").first()

if existing_user is None:
    hashed_password = bcrypt.hashpw("algebra".encode('utf-8'), bcrypt.gensalt())
    predefined_user = User(username="admin", password=hashed_password.decode('utf-8'))
    session.add(predefined_user)
    session.commit()
else:
    print("Admin user already exists, skipping initialization.")