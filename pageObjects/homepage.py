from selenium.webdriver.common.by import By

class HomePage:
    add_backpack_btn_id ="add-to-cart-sauce-labs-backpack"
    cart_badge_class = "shopping_cart_badge"

    def __init__(self, driver):
        self.driver = driver

    def click_add_backpack(self):
        """Click Add to Cart for backpack."""
        self.driver.find_element(By.ID, self.add_backpack_btn_id).click()

    def get_cart_count(self):
        """Return cart count text (e.g., '1')."""
        return self.driver.find_element(By.CLASS_NAME, self.cart_badge_class).text

    def get_backpack_button_text(self):
        """Return text on the backpack button (Add to cart / Remove)."""
        return self.driver.find_element(By.ID, self.add_backpack_btn_id).text
