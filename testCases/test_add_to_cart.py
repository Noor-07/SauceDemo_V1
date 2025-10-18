from configurations import config
from pageObjects.homepage import HomePage
from pageObjects.loginpage import LoginPage


class Test_AddToCart:
    def test_add_backpack(self,setup):
        driver = setup
        driver.get(config.baseURL)

        lp = LoginPage(driver)
        lp.set_username(config.username)
        lp.set_password(config.password)
        lp.click_login()

        hp = HomePage(driver)
        hp.click_add_backpack()

        cart_count = hp.get_cart_count()
        assert cart_count == "1"

