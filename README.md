# 🛒 FastAPI E-Commerce Backend

A production-ready E-Commerce Backend API built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**.

## 🚀 Features

- User Registration & Login
- JWT Authentication
- Role-Based Authorization (Admin/User)
- Product Management (CRUD)
- Category Management
- Shopping Cart
- Order Management
- Payment Integration (Razorpay)
- Image Upload Support
- PostgreSQL Database
- Interactive Swagger API Documentation

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Razorpay
- Uvicorn
- Git & GitHub

---

## 📂 Project Structure

```
app/
├── database/
├── models/
├── routers/
├── schemas/
├── services/
├── payments/
├── auth.py
├── oauth2.py
└── main.py
```

---

## 🔐 Authentication

- User Registration
- User Login
- JWT Token Generation
- Protected Routes
- Admin-only APIs

---

## 📦 API Modules

- Users
- Categories
- Products
- Shopping Cart
- Orders
- Payments

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/syedahmedsayeedx7/fastapi-ecommerce-backend.git
```

### Go to the project

```bash
cd fastapi-ecommerce-backend
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ PostgreSQL Configuration

Update your database URL inside your project configuration:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/ecommerce"
```

---

## ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 📸 Sample APIs

- User Registration
- Login
- Create Category
- Create Product
- Add to Cart
- Place Order
- Make Payment

---

## 📈 Future Improvements

- Docker Support
- CI/CD
- Deployment
- Email Verification
- Product Reviews
- Wishlist
- Coupons
- Inventory Management

---

## 👨‍💻 Author

**Syed Ahmed Sayeed**

GitHub:
https://github.com/syedahmedsayeedx7

---

## ⭐ If you found this project useful, consider giving it a star!