import pytest
from Checkout import Checkout


class TestClassCheckout:

    @pytest.fixture()
    def checkout(self):
        checkout = Checkout()
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        return checkout

    def test_can_calculate_total(self, checkout):
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_get_correct_total_with_multiple_items(self, checkout):
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_can_add_discount_rule(self, checkout):
        checkout.addDiscount("a", 3, 2)

    def test_canApplyDiscountRule(self, checkout):
        checkout.addDiscount("a", 3, 2)
        checkout.addItem("a")
        checkout.addItem("a")
        checkout.addItem("a")
        assert checkout.calculateTotal() == 2

    def test_exception_with_bad_item(self, checkout):
        with pytest.raises(Exception):
            checkout.addItem("c")
