# -*- coding: utf-8 -*-
"""Testy pytest dla nowej metody apply_discount klasy Product.

Uruchomienie: pytest test_product_discount.py -v
"""

import pytest
from product import Product


@pytest.fixture
def product():
    """Tworzy instancje Product z cena 100.0 do testow."""
    return Product("Test Product", 100.0, 10)


@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),      
    (50, 50.0),      
    (100, 0.0),      
    (25, 75.0),      
    (10, 90.0),      
])
def test_apply_discount_valid(product, percent, expected_price):
    """Testuje apply_discount z walidnymi wartościami procentowymi."""
    product.apply_discount(percent)
    assert product.price == expected_price


@pytest.mark.parametrize("percent", [
    -1,      
    -50,     
    101,     
    150,     
])
def test_apply_discount_invalid_raises(product, percent):
    """Testuje apply_discount z nieprawidłowymi wartościami (ValueError)."""
    with pytest.raises(ValueError):
        product.apply_discount(percent)


def test_apply_discount_multiple_times(product):
    """Testuje zastosowanie zniżki wielokrotnie."""
    product.apply_discount(50)
    assert product.price == 50.0
    
    product.apply_discount(50)
    assert product.price == 25.0


def test_apply_discount_affects_total_value(product):
    """Testuje czy zmiana ceny poprzez apply_discount zmienia total_value."""
    initial_total = product.total_value()
    product.apply_discount(50)
    expected_total = 50.0 * 10
    assert product.total_value() == expected_total
    assert product.total_value() < initial_total
