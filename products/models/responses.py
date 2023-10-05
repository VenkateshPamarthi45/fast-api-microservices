

class ProductResponse:
    id: str
    name: str
    description: str
    price: int

    def __init__(self, product_id, name, description, price):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
