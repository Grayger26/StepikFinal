from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def should_be_no_products_in_basket(self):
        basket_text = self.browser.find_element(*BasePageLocators.BASKET_TEXT).text
        assert "Your basket is empty" in basket_text, "Basket is not empty"


