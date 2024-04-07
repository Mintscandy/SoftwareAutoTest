from M3M.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    url = "/login"
    username_loc = (By.CLASS_NAME, "username",)
    password_loc = (By.NAME, "password",)
    login_loc = (By.ID, "signIn",)

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_login(self):
        self.find_element(*self.login_loc).click()


def test_login_page(driver, username, password):
    login = LoginPage(driver)
    login.open()
    login.type_username(username)
    login.type_password(password)
    login.type_login()
