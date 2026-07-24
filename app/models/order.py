from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.database import Base



class Order(Base):

    __tablename__ = "orders"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    total_price = Column(
        Float
    )


    status = Column(
        String,
        default="Pending Payment"
    )


    payment_status = Column(
        String,
        default="Not Paid"
    )


    payment_id = Column(
        String,
        nullable=True
    )


    user = relationship(
        "User",
        back_populates="orders"
    )


    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete"
    )