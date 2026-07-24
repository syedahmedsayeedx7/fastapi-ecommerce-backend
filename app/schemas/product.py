from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.category_response import CategoryResponse


class ProductCreate(BaseModel):

    name: str = Field(..., min_length=2)

    price: float = Field(..., gt=0)

    description: str

    category_id: int


class Product(ProductCreate):

    id: int

    image: Optional[str] = None

    category: CategoryResponse

    class Config:
        from_attributes = True