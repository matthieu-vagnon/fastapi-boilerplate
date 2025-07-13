from pydantic import BaseModel, UUID4
from datetime import date
from uuid import uuid4


class User(BaseModel):
    id: UUID4 = uuid4()
    name: str
    created_on: date

    class Config:
        orm_mode = True
