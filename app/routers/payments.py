from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services import payment_service

from app.schemas.payment import PaymentVerify



router=APIRouter(

    prefix="/payments",

    tags=["Payments"]

)




@router.post("/create/{order_id}")

def create_payment(

    order_id:int,

    db:Session=Depends(get_db)

):


    return payment_service.create_payment(

        db,

        order_id

    )






@router.post("/verify/{order_id}")

def verify_payment(

    order_id:int,

    data:PaymentVerify,

    db:Session=Depends(get_db)

):


    return payment_service.verify_payment(

        db,

        order_id,

        data

    )






@router.get("/history/{order_id}")

def history(

    order_id:int,

    db:Session=Depends(get_db)

):


    return payment_service.payment_history(

        db,

        order_id

    )