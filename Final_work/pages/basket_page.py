from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET
        ), "Basket is not empty"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET
        ), "Basket is empty"

    def should_not_be_empty_cart_message(self):
        assert not self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET
        ), "Basket is not empty"
