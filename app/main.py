from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.database import engine, Base


# Import all models BEFORE create_all
from app.models.category import Category
from app.models.user import User
from app.models.product import Product
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.payment import Payment


# Import routers
from app.routers.products import router as product_router
from app.routers.category import router as category_router
from app.routers.user import router as user_router
from app.routers import cart
from app.routers import orders
from app.routers import payments


app = FastAPI(
    title="My E-Commerce API",
    version="1.0.0"
)


# Create PostgreSQL database tables
Base.metadata.create_all(bind=engine)


# Serve uploaded product images
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)


# Register API routes
app.include_router(product_router)
app.include_router(category_router)
app.include_router(user_router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(payments.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to My E-Commerce API"
    }