from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.settings import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

print("DB URL:", settings.database_url)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
