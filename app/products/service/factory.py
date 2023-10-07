from fastapi import Depends

from app.products.service.product_service import ProductService


def get_product_service(service=Depends(ProductService)):
    return service
