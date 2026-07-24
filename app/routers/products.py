from typing import List
import os
import shutil

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.product import ProductCreate, Product as ProductResponse
from app.services import product_service
from app.oauth2 import admin_required

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- CREATE PRODUCT ---------------- #

@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return product_service.create_product(db, product)


# ---------------- UPLOAD IMAGE ---------------- #

@router.post("/{product_id}/upload-image")
def upload_image(
    product_id: int,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    product = product_service.get_product_by_id(
        db,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    os.makedirs("uploads", exist_ok=True)

    filename = f"{product_id}_{image.filename}"

    filepath = os.path.join(
        "uploads",
        filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            image.file,
            buffer
        )

    product_service.update_product_image(
        db,
        product_id,
        filename
    )

    return {
        "message": "Image uploaded successfully",
        "filename": filename
    }


# ---------------- SEARCH ---------------- #

@router.get("/search", response_model=List[ProductResponse])
def search_products(
    name: str,
    db: Session = Depends(get_db)
):
    return product_service.search_products(
        db,
        name
    )


# ---------------- ALL PRODUCTS ---------------- #

@router.get("/all", response_model=List[ProductResponse])
def get_all_products(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return product_service.get_all_products(
        db,
        skip,
        limit
    )


# ---------------- SORT ---------------- #

@router.get("/sort", response_model=List[ProductResponse])
def sort_products(
    order: str = "asc",
    db: Session = Depends(get_db)
):
    return product_service.sort_products(
        db,
        order
    )


# ---------------- CATEGORY ---------------- #

@router.get("/category/{category_id}", response_model=List[ProductResponse])
def filter_by_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return product_service.filter_by_category(
        db,
        category_id
    )


# ---------------- PRICE ---------------- #

@router.get("/price", response_model=List[ProductResponse])
def filter_by_price(
    min_price: float,
    max_price: float,
    db: Session = Depends(get_db)
):
    return product_service.filter_by_price(
        db,
        min_price,
        max_price
    )


# ---------------- GET PRODUCT ---------------- #

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = product_service.get_product_by_id(
        db,
        product_id
    )

    if product is None:
        return {
            "message": "Product not found"
        }

    return product


# ---------------- UPDATE ---------------- #

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    updated = product_service.update_product(
        db,
        product_id,
        product
    )

    if updated is None:
        return {
            "message": "Product not found"
        }

    return updated


# ---------------- DELETE ---------------- #

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    deleted = product_service.delete_product(
        db,
        product_id
    )

    if deleted is None:
        return {
            "message": "Product not found"
        }

    return deleted