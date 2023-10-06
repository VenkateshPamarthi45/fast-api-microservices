from fastapi import FastAPI, Request

from app.products import products
from app.handlers.custom_exceptions import ProductNotFoundException
from fastapi.responses import JSONResponse


app = FastAPI()
app.include_router(products.router, prefix="/v1/products")


@app.exception_handler(ProductNotFoundException)
def product_not_found_exception_handler(req: Request, ex: ProductNotFoundException):
    return JSONResponse(
        status_code=ex.status_code,
        content={"message": f"error: {ex.message}"}
    )


@app.get("/index")
def index():
    return {"message": "welcome Venky"}
