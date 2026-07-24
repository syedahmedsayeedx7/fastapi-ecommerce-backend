from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.category import CategoryCreate
from app.services import category_service

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, category)


@router.get("/")
def get_all_categories(db: Session = Depends(get_db)):
    return category_service.get_all_categories(db)


@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = category_service.get_category_by_id(db, category_id)

    if category is None:
        return {"message": "Category not found"}

    return category


@router.put("/{category_id}")
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    updated = category_service.update_category(db, category_id, category)

    if updated is None:
        return {"message": "Category not found"}

    return updated


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted = category_service.delete_category(db, category_id)

    if deleted is None:
        return {"message": "Category not found"}

    return deleted