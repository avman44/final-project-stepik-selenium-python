from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element_by_tag_name("h1").text
    product_price = browser.find_element_by_class_name("price_color").text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_add_to_basket_message(product_name)
    page.should_be_basket_price(product_price)