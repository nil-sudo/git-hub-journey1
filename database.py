from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# We need to URL-encode the password if it has special characters like '@'
import urllib.parse
# Using the Supabase Connection Pooler (Seoul Region - IPv4 compatible)
project_id = ""
password =
db_host = ""

SQLALCHEMY_DATABASE_URL = f""

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
