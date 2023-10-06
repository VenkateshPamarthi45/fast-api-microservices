from uuid import UUID


class Product:
    id: str
    name: str
    description: str
    price: int

    def __init__(self, uuid: str, name: str, description: str, price: int) -> object:
        self.price = price
        self.description = description
        self.name = name
        self.id = uuid
