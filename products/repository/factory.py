from fastapi import Depends

from products.repository.product_repository import ProductRepository


def get_product_repo(repo=Depends(ProductRepository)):
    return repo
