from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services import order_service



router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)



USER_ID = 1




# Place Order

@router.post("/place")
def place_order(
    db:Session=Depends(get_db)
):

    return order_service.place_order(
        db,
        USER_ID
    )





# Order History

@router.get("/")
def order_history(
    db:Session=Depends(get_db)
):

    return order_service.get_orders(
        db,
        USER_ID
    )





# Order Details

@router.get("/{order_id}")
def order_details(
    order_id:int,
    db:Session=Depends(get_db)
):

    return order_service.get_order_details(
        db,
        order_id
    )