"""Database connection helpers."""
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from src.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def get_database_connection() -> Connection:
  url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
  engine = create_engine(url)
  return engine.connect()
