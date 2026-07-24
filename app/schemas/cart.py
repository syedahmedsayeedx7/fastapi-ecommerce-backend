from pydantic import BaseModel


class CartItemCreate(BaseModel):

    product_id:int

    quantity:int = 1



class CartItemUpdate(BaseModel):

    quantity:int



class ProductResponse(BaseModel):

    id:int

    name:str

    price:float

    class Config:
        from_attributes=True



class CartItemResponse(BaseModel):

    id:int

    quantity:int

    product:ProductResponse


    class Config:
        from_attributes=True



class CartResponse(BaseModel):

    id:int

    items:list[CartItemResponse]


    class Config:
        from_attributes=True