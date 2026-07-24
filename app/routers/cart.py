from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services import cart_service

from app.schemas.cart import (
    CartItemCreate,
    CartItemUpdate,
    CartResponse
)

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

# Temporary user ID
USER_ID = 1


@router.post("/add")
def add_cart(
    data: CartItemCreate,
    db: Session = Depends(get_db)
):
    return cart_service.add_product_to_cart(
        db,
        USER_ID,
        data.product_id,
        data.quantity
    )


@router.get("/", response_model=CartResponse)
def view_cart(
    db: Session = Depends(get_db)
):
    return cart_service.get_or_create_cart(
        db,
        USER_ID
    )


@router.delete("/{item_id}")
def remove_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    return cart_service.remove_cart_item(
        db,
        item_id
    )


@router.put("/{item_id}")
def update_item(
    item_id: int,
    data: CartItemUpdate,
    db: Session = Depends(get_db)
):
    return cart_service.update_quantity(
        db,
        item_id,
        data.quantity
    )