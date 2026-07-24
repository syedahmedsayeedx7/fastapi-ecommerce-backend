from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)


class Category(CategoryCreate):
    id: int

    class Config:
        from_attributes = True