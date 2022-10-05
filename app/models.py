from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import DATABASE_URL


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(binds=engine.connect())
    return session
