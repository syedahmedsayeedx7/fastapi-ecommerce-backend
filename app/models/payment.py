from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database.database import Base



class Payment(Base):

    __tablename__ = "payments"


    id = Column(
        Integer,
        primary_key=True
    )


    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )


    razorpay_order_id = Column(
        String
    )


    razorpay_payment_id = Column(
        String,
        nullable=True
    )


    razorpay_signature = Column(
        String,
        nullable=True
    )


    amount = Column(
        Float
    )


    status = Column(
        String,
        default="Pending"
    )