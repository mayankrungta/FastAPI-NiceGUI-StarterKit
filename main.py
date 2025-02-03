from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, courses

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

app.include_router(users.router)
app.include_router(courses.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
