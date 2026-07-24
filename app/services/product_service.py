from sqlalchemy.orm import Session
from app.models.product import Product


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product):
    new_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        category_id=product.category_id,
        image=None
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def update_product(db: Session, product_id: int, updated_product):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        return None

    product.name = updated_product.name
    product.price = updated_product.price
    product.description = updated_product.description
    product.category_id = updated_product.category_id

    db.commit()
    db.refresh(product)

    return product


def update_product_image(
    db: Session,
    product_id: int,
    filename: str
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None

    product.image = filename

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}


def search_products(db: Session, name: str):
    return db.query(Product).filter(
        Product.name.contains(name)
    ).all()


def get_all_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


def sort_products(db: Session, order: str):
    if order.lower() == "desc":
        return db.query(Product).order_by(
            Product.price.desc()
        ).all()

    return db.query(Product).order_by(
        Product.price.asc()
    ).all()


def filter_by_category(db: Session, category_id: int):
    return db.query(Product).filter(
        Product.category_id == category_id
    ).all()


def filter_by_price(
    db: Session,
    min_price: float,
    max_price: float
):
    return db.query(Product).filter(
        Product.price >= min_price,
        Product.price <= max_price
    ).all()