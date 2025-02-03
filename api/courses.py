from typing import Optional, List
import fastapi
from fastapi import Path, Query
from pydantic import BaseModel

router = fastapi.APIRouter()


class Course(BaseModel):
    title: str
    description: Optional[str] = None
    credits: int


courses: List[Course] = []


@router.post("/courses")
async def create_course(course: Course):
    courses.append(course)
    return {"message": f"Course '{course.title}' created successfully"}


@router.get("/courses", response_model=List[Course])
async def get_courses():
    return courses


@router.get("/courses/{course_id}")
async def get_course(course_id: int = Path(..., description="The ID of the course to retrieve", gt=-1)):
    return courses[course_id]
