from fastapi import FastAPI

from models.requests import ProductRequest
from models.responses import ProductResponse

app = FastAPI()


@app.get("/index")
def index():
    return {"message": "welcome Venky"}


products = {}


@app.get("/v1/products/{product_id}")
def get_product(product_id: str):
    if products.get(product_id) is None:
        return {"message": "product not exist"}
    else:
        return products.get(product_id)


@app.post("/v1/products", response_model=ProductResponse)
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
