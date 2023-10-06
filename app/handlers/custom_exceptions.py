from fastapi import HTTPException


class ProductNotFoundException(HTTPException):
    status_code: int
    message: str

    def __init__(self):
        self.status_code = 404
        self.message = "Product Not found"
