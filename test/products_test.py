import unittest
from unittest.mock import Mock, MagicMock

from fastapi import Depends
from fastapi.testclient import TestClient

from app.handlers.custom_exceptions import ProductNotFoundException
from app.products.data.product import Product
from app.products.models.responses import ProductResponse
from app.products.products import get_product
from app.products.repository.factory import get_product_repo
from app.products.repository.product_repository import ProductRepository
from app.products.service.product_service import ProductService
from app.products import products
from main import app

client = TestClient(app)


class ProductServiceTestCase(unittest.TestCase):

    def test_get_product_no_product(self):
        thing = ProductRepository()
        thing.get_product = MagicMock(return_value="no")
        service = ProductService(thing)
        result = service.get_product_detail("1")
        self.assertEqual(result, "no")

    def test_get_product_with_product(self):
        thing = ProductRepository()
        thing.get_product = MagicMock(return_value=Product(uuid="1", name="asdasd", description="sad", price=1200))
        service = ProductService(thing)
        result = service.get_product_detail("1")
        self.assertIsInstance(result, ProductResponse)
        self.assertEqual(result.id, "1")
        self.assertEqual(result.name, "asdasd")
        self.assertEqual(result.description, "sad")
        self.assertEqual(result.price, 1200)


class ProductRouterTestCase(unittest.TestCase):

    def test_get_product_no_product(self):
        thing = ProductService()
        thing.get_product_detail = MagicMock(return_value="ss")
        response = client.get("/v1/products/1")
        assert response.status_code == 404
        assert response.json() == {'message': 'error: Product Not found'}


if __name__ == '__main__':
    unittest.main()
