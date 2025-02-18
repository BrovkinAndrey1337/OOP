import json

from src.classes import Category, Product


def load_classes_from_data(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories


if __name__ == "__main__":
    categories = load_classes_from_data("../data/products.json")
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        for product in category.products:
            print(
                f"  Продукт: {product.name}, Цена: {product.price}, Количество: {product.quantity}"
            )
