from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency to get the database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sections/", response_model=schemas.Section)
def create_section(section: schemas.SectionCreate, db: Session = Depends(get_db)):
    db_section = crud.get_section_by_name(db, name=section.name)
    if db_section:
        raise HTTPException(
            status_code=400, detail="Section already registered")
    return crud.create_section(db=db, section=section)


@router.get("/sections/", response_model=List[schemas.Section])
def read_sections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, skip=skip, limit=limit)
    return sections


@router.get("/sections/{section_id}", response_model=schemas.Section)
def read_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section


@router.put("/sections/{section_id}", response_model=schemas.Section)
def update_section(section_id: int, section: schemas.SectionUpdate, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return crud.update_section(db=db, section=section, section_id=section_id)


@router.delete("/sections/{section_id}", response_model=schemas.Section)
def delete_section(section_id: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, section_id=section_id)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return crud.delete_section(db=db, section_id=section_id)
