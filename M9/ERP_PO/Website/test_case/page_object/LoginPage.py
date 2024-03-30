from selenium.webdriver.common.by import By

from M9.ERP_PO.Website.test_case.page_object.BasePage import *


class LoginPage(Page):
    url = "/login"
    username_loc = (By.CLASS_NAME, "username",)
    password_loc = (By.ID, "password",)
    login_loc = (By.TAG_NAME, "button",)

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_login(self):
        self.find_element(*self.login_loc).click()


def test_login_page(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login()
