from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models.base import Item

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items")
def list_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@router.post("/items")
def create_item(name: str, value: int, db: Session = Depends(get_db)):
    item = Item(name=name, value=value)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
