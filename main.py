from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    # name: str
    email: str
    is_active: Optional[bool] = False
    full_name: Optional[str] = None
    phone: Optional[int] = None


users: List[User] = []

app = FastAPI(
    title="LMS Users API",
    description="API for managing users",
    version="1.0.0",
    contact={
        "name": "John Doe",
        "email": "G1t0O@example.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0"
    }
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": f"User {user} created successfully"}


@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(...,
                        description="The ID of the user to retrieve", gt=-2),
    # is_active: Optional[bool] = False
    is_active: Optional[str] = Query(None, max_length=3)
):
    return users[user_id]
