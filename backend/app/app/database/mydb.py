from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings
from typing import Generator
from sqlalchemy.orm import sessionmaker


engine = create_engine(settings.DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_mydb_session() -> Generator:
    try:
        mydb = SessionLocal()
        yield mydb
    finally:
        mydb.close()