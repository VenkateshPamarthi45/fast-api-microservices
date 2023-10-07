from fastapi import Depends

from app.products.models.requests import ProductRequest
from app.products.models.responses import ProductResponse
from app.products.repository.factory import get_product_repo
from app.products.repository.product_repository import ProductRepository


class ProductService:
    def __init__(self, repo=Depends(ProductRepository)):
        self.repo = repo

    def get_product_detail(self, id):
        if id is None:
            return "Id is empty"
        else:
            product = self.repo.get_product(id)
            if isinstance(product, str):
                return product
            else:
                return ProductResponse(
                    product_id=product.id,
                    name=product.name,
                    description=product.description,
                    price=product.price,
                )

    def new_product(self, product_request: ProductRequest):
        if len(product_request.name) == 0:
            return "Name is empty"
        elif len(product_request.description) == 0:
            return "Description is empty"
        elif product_request.price <= 0:
            return "Price is less than equal to 0"
        else:
            product = self.repo.create_product(
                name=product_request.name,
                description=product_request.description,
                price=product_request.price,
            )
            return ProductResponse(
                product_id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
            )
