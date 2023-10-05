from fastapi import APIRouter

from handlers.custom_exceptions import ProductNotFoundException
from products.models.requests import ProductRequest
from products.models.responses import ProductResponse

router = APIRouter()

products = {}


@router.get("/{product_id}")
def get_product(product_id: str):
    if products.get(product_id) is None:
        raise ProductNotFoundException()
    else:
        return products.get(product_id)


@router.post("")
def create_product(product: ProductRequest):
    if len(product.name) == 0:
        return "Name is empty"
    elif len(product.description) == 0:
        return "description is empty"
    elif product.price <= 0:
        return "Price is less than equal to 0"
    else:
        new_product_id = str(len(products.keys()) + 1)
        product_response = ProductResponse(product_id=new_product_id, name=product.name,
                                           description=product.description,
                                           price=product.price)
        products[new_product_id] = product_response
        return product_response
