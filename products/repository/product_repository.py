from products.data.product import Product


class ProductRepository:
    products = {}

    def create_product(self, name: str, description: str, price: int):
        new_product_id = str(len(self.products.keys()) + 1)
        product = Product(uuid=new_product_id, name=name, description=description, price=price)
        self.products[new_product_id] = product
        return product

    def get_products(self):
        return self.products

    def get_product(self, product_id):
        if str(product_id) in self.products:
            return self.products[product_id]
        else:
            return "No product found"

