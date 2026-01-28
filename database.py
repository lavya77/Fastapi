from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine


db_url="postgresql://postgres:blehh@localhost:5432/fast"
engine = create_engine(db_url)
session = sessionmaker( autoflush=False,bind=engine,autocommit=False)