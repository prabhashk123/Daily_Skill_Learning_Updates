from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://127.0.0:5432/employee_db/?user=postgres$password=postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={}, future= True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future= True
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    

