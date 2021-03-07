from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.LINK_TEXT, "View basket")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(), \"basket is empty\")]")