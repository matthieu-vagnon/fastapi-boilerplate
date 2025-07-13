from core.database import engine, Base
from core.models.users import UserDB

Base.metadata.create_all(bind=engine)
