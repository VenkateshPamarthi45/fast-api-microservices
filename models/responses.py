from typing import Any

from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    price: int

    def __init__(self, product_id, name, description, price, **data: Any):
        super().__init__(**data)
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
