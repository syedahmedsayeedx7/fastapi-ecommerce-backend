from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.database import Base


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(String, nullable=False)


    email = Column(
        String,
        unique=True,
        nullable=False
    )


    hashed_password = Column(
        String,
        nullable=False
    )


    is_admin = Column(
        Boolean,
        default=False
    )


    cart = relationship(
        "Cart",
        back_populates="user",
        uselist=False
    )


    orders = relationship(
        "Order",
        back_populates="user"
    )