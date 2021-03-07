from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_items_in_basket()
        self.should_be_message_about_basket_is_empty()

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There is an item in the basket, but should not be"

    def should_be_message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "Missing message \"basket is empty\""
