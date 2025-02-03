from typing import Optional, List
import fastapi
from fastapi import Path, Query
from pydantic import BaseModel


class User(BaseModel):
    # name: str
    email: str
    is_active: Optional[bool] = False
    full_name: Optional[str] = None
    phone: Optional[int] = None


users: List[User] = []

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": f"User {user} created successfully"}


@router.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(...,
                        description="The ID of the user to retrieve", gt=-2),
    # is_active: Optional[bool] = False
    is_active: Optional[str] = Query(None, max_length=3)
):
    return users[user_id]
