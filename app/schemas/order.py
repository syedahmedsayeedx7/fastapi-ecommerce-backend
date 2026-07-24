from pydantic import BaseModel



class OrderItemResponse(BaseModel):

    id:int

    product_id:int

    quantity:int

    price:float


    class Config:
        from_attributes=True




class OrderResponse(BaseModel):

    id:int

    total_price:float

    status:str

    items:list[OrderItemResponse]


    class Config:
        from_attributes=True