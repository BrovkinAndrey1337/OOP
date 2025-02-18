from typing import List


class Product:
    """Класс продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категорий продуктов"""

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_products += len(products)
