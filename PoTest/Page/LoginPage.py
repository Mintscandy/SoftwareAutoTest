from PoTest.Page.BasePage import *
from selenium.webdriver.common.by import By
class LoginPage(Page):
    username_loc = (By.ID,"username")

    def type(self,user):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(user)
def test_login_page(driver,username,password):
    pass