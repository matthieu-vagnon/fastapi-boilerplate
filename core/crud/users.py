from sqlalchemy.orm import Session
from core.models.users import UserDB
from pydantic import UUID4
from datetime import date
from core.exceptions import UserNotFoundError, UserAlreadyExistError


def get_all_users(db: Session):
    users = db.query(UserDB).all()

    return users


def get_user_by_id(user_id: UUID4, db: Session):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise UserNotFoundError()

    return user


def create_new_user(user_name: str, db: Session):
    new_user = UserDB(name=user_name, created_on=date.today())
    name_exists = db.query(UserDB).filter(UserDB.name == user_name).first()

    if name_exists:
        raise UserAlreadyExistError()

    db.add(new_user)
    db.commit()

    return new_user


def delete_user_by_id(user_id: UUID4, db: Session):
    user_to_delete = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user_to_delete:
        raise UserNotFoundError()

    db.delete(user_to_delete)
    db.commit()
