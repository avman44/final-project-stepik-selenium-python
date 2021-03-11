from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_add_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_adding_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDING_MESSAGE).text
        assert product_name == product_name_in_adding_message, "product names do not match"

    def should_be_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_ADDING_MESSAGE).text
        print("product_price = ",product_price,"  basket_price = ", basket_price)
        assert product_price == basket_price, "product prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be dissappeared"
