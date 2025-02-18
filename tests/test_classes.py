import pytest

from src.classes import Category, Product


@pytest.fixture
def product_koumiss():
    product = Product("Кумыс", "Райское наслаждение", 13.37, 5)
    return product


@pytest.fixture
def product_beer():
    product = Product("Пиво", "Будущее будет светлым и нефильтрованным", 22.8, 1)
    return product


def test_product_koumiss(product_koumiss, product_beer):
    assert product_koumiss.name == "Кумыс"
    assert product_koumiss.description == "Райское наслаждение"
    assert product_koumiss.price == 13.37
    assert product_koumiss.quantity == 5
    assert product_beer.name == "Пиво"
    assert product_beer.description == "Будущее будет светлым и нефильтрованным"
    assert product_beer.price == 22.8
    assert product_beer.quantity == 1


@pytest.fixture
def category_of_2_products(product_koumiss, product_beer):
    category1 = Category(
        "2 на выбор", "Выбирай любое, не ошибешься", [product_beer, product_koumiss]
    )
    category2 = Category("1 на выбор", "Возьми меня", [product_beer])
    return category1, category2


def test_category_of_products(category_of_2_products):
    category1, category2 = category_of_2_products

    assert category1.name == "2 на выбор"
    assert category1.description == "Выбирай любое, не ошибешься"
    assert len(category1.products) == 2
    assert category1.products[0].name == "Пиво"
    assert category1.products[1].name == "Кумыс"

    assert category2.name == "1 на выбор"
    assert category2.description == "Возьми меня"
    assert len(category2.products) == 1
    assert category2.products[0].name == "Пиво"

    assert Category.total_categories == 2
