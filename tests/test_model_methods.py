import pytest

from app.orm.models.discount.discount import ProductDiscountModel
from app.orm.models.product.category_model import CategoryModel
from app.orm.models.product.product_model import ProductModel


@pytest.fixture
def category_parent_exists():
    category = CategoryModel()
    parent_category = CategoryModel()
    parent_category.id = 1
    category.parent_object = parent_category
    return category


@pytest.fixture
def category_no_parent():
    category = CategoryModel()
    return category


@pytest.fixture
def product_with_discount():
    product = ProductModel()
    discount1 = ProductDiscountModel()
    discount2 = ProductDiscountModel()
    discount1.amount = 0.01
    discount2.amount = 0.10
    product.product_discount = [discount1, discount2]
    return product


def test_parent_categories_exsists(category_parent_exists):
    assert category_parent_exists.parent_categories() == [1]


def test_no_parent_categories(category_no_parent):
    assert category_no_parent.parent_categories() == []


def test_total_discount(product_with_discount):
    assert product_with_discount.total_discount == 0.11
