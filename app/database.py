from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = os.getenv("DATABASE_URL").replace(
    "postgres://", "postgresql+psycopg2://"
)
print(f"DATABASE_URL: {DATABASE_URL}")  # Debug print
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:3bkr%402251998@db:5432/task_manager_db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
