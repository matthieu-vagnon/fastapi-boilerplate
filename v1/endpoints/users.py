from fastapi import APIRouter, Query, Depends, Path, status, HTTPException
from core.schemas.users import User
from sqlalchemy.orm import Session
from core.database import get_db
from core.crud.users import (
    get_all_users,
    get_user_by_id,
    create_new_user,
    delete_user_by_id,
)
from pydantic import UUID4
from core.exceptions import UserNotFoundError, UserAlreadyExistError
from typing import Annotated

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[User], summary="Get all the users.")
async def get_users(
    db: Annotated[Session, Depends(get_db)],
):
    return get_all_users(db)


@router.get(
    "/{user_id}", response_model=User, summary="Get a user based on his unique ID."
)
async def get_user(
    user_id: Annotated[UUID4, Path()], db: Annotated[Session, Depends(get_db)]
):
    try:
        return get_user_by_id(user_id, db)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail="User not found.")


@router.post("/", response_model=User, summary="Create a new user.")
async def add_user(
    user_name: Annotated[str, Query()], db: Annotated[Session, Depends(get_db)]
):
    try:
        return create_new_user(user_name, db)
    except UserAlreadyExistError:
        raise HTTPException(status_code=403, detail="User name already exist.")


@router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a user."
)
async def delete_user(
    user_id: Annotated[UUID4, Path()], db: Annotated[Session, Depends(get_db)]
):
    try:
        delete_user_by_id(user_id, db)
    except UserNotFoundError:
        raise HTTPException(
            status_code=404, detail="No user was found with the provided ID."
        )
