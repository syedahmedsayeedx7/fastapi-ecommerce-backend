from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    price = Column(Float)

    description = Column(String)

    image = Column(
        String,
        nullable=True
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    category = relationship(
        "Category",
        back_populates="products"
    )

    cart_items = relationship(
        "CartItem",
        back_populates="product"
    )