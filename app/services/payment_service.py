from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.payment import Payment

from app.payments.razorpay_client import client




def create_payment(
        db:Session,
        order_id:int
):


    order=db.query(Order).filter(
        Order.id==order_id
    ).first()



    if not order:
        return None



    razorpay_order = client.order.create(
        {
            "amount":int(order.total_price*100),

            "currency":"INR",

            "payment_capture":1
        }
    )



    payment=Payment(

        order_id=order.id,

        razorpay_order_id=razorpay_order["id"],

        amount=order.total_price,

        status="Created"
    )



    db.add(payment)

    db.commit()

    db.refresh(payment)



    return razorpay_order





def verify_payment(
        db:Session,
        order_id:int,
        data
):


    try:


        client.utility.verify_payment_signature(

            {

            "razorpay_order_id":
            data.razorpay_order_id,


            "razorpay_payment_id":
            data.razorpay_payment_id,


            "razorpay_signature":
            data.razorpay_signature

            }

        )



        payment=db.query(Payment).filter(

            Payment.order_id==order_id

        ).first()



        if payment:


            payment.razorpay_payment_id = (
                data.razorpay_payment_id
            )


            payment.razorpay_signature = (
                data.razorpay_signature
            )


            payment.status="Success"



        order=db.query(Order).filter(

            Order.id==order_id

        ).first()



        if order:


            order.payment_status="Paid"

            order.status="Confirmed"



        db.commit()



        return {

            "message":
            "Payment successful",

            "order_status":
            "Confirmed"

        }



    except Exception:


        return {

            "message":
            "Payment verification failed"

        }





def payment_history(
        db:Session,
        order_id:int
):

    return db.query(Payment).filter(

        Payment.order_id==order_id

    ).all()