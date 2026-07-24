from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.order import Order
from app.models.order_item import OrderItem



def place_order(
        db:Session,
        user_id:int
):

    cart=db.query(Cart).filter(
        Cart.user_id==user_id
    ).first()



    if not cart or len(cart.items)==0:

        return None



    total=0


    order=Order(
        user_id=user_id,
        total_price=0,
        status="Placed"
    )


    db.add(order)

    db.commit()

    db.refresh(order)



    for item in cart.items:


        item_total = (
            item.product.price *
            item.quantity
        )


        total += item_total



        order_item=OrderItem(

            order_id=order.id,

            product_id=item.product_id,

            quantity=item.quantity,

            price=item.product.price
        )


        db.add(order_item)



    order.total_price=total



    # clear cart

    for item in cart.items:

        db.delete(item)



    db.commit()

    db.refresh(order)


    return order





def get_orders(
        db:Session,
        user_id:int
):

    return db.query(Order).filter(
        Order.user_id==user_id
    ).all()





def get_order_details(
        db:Session,
        order_id:int
):

    return db.query(Order).filter(
        Order.id==order_id
    ).first()