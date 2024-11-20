from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# from pydantic import BaseModel
from app.database import SessionLocal
from app.models.testModel import Item
from app.schema.test_schema import ItemCreate

# class ItemCreate(BaseModel):
    # name: str
    # description: str

test_router = APIRouter(prefix="/items", tags=["Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@test_router.get("/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@test_router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
