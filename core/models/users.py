from sqlalchemy import Column, String, Date
from core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class UserDB(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    created_on = Column(Date, nullable=False)
