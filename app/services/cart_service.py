from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product import Product


def get_or_create_cart(db: Session, user_id: int):

    cart = db.query(Cart).filter(
        Cart.user_id == user_id
    ).first()

    if not cart:
        cart = Cart(
            user_id=user_id
        )

        db.add(cart)
        db.commit()
        db.refresh(cart)

    return cart


def add_product_to_cart(
    db: Session,
    user_id: int,
    product_id: int,
    quantity: int
):

    # Check if product exists
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {
            "message": "Product not found"
        }

    # Get user's cart
    cart = get_or_create_cart(
        db,
        user_id
    )

    # Check if product already exists in cart
    item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product_id
    ).first()

    if item:
        item.quantity += quantity
    else:
        item = CartItem(
            cart_id=cart.id,
            product_id=product_id,
            quantity=quantity
        )

        db.add(item)

    db.commit()
    db.refresh(item)

    return {
        "message": "Product added successfully",
        "cart_item_id": item.id,
        "product": product.name,
        "quantity": item.quantity
    }


def remove_cart_item(
    db: Session,
    item_id: int
):

    item = db.query(CartItem).filter(
        CartItem.id == item_id
    ).first()

    if not item:
        return {
            "message": "Item not found"
        }

    db.delete(item)
    db.commit()

    return {
        "message": "Item removed successfully"
    }


def update_quantity(
    db: Session,
    item_id: int,
    quantity: int
):

    item = db.query(CartItem).filter(
        CartItem.id == item_id
    ).first()

    if not item:
        return {
            "message": "Item not found"
        }

    item.quantity = quantity

    db.commit()
    db.refresh(item)

    return {
        "message": "Quantity updated",
        "quantity": item.quantity
    }