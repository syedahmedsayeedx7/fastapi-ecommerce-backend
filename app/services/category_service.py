from sqlalchemy.orm import Session
from app.models.category import Category


def create_category(db: Session, category):
    new_category = Category(name=category.name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


def get_all_categories(db: Session):
    return db.query(Category).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db: Session, category_id: int, updated_category):
    category = db.query(Category).filter(Category.id == category_id).first()

    if category is None:
        return None

    category.name = updated_category.name

    db.commit()
    db.refresh(category)

    return category


def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if category is None:
        return None

    db.delete(category)
    db.commit()

    return {"message": "Category deleted successfully"}