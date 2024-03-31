from selenium import webdriver
from M10.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    url = "/login"
    username_loc = (By.ID, "username",)
    password_loc = (By.NAME, "password",)
    login_loc = (By.CLASS_NAME, "el-button",)

    def type_username(self, usr):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(usr)

    def type_password(self, pwd):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(pwd)

    def type_login(self):
        self.find_element(*self.login_loc).click()


def test_login_page(driver, username, password):
    login = LoginPage(driver)
    login.open()
    login.type_username(username)
    login.type_password(password)
    login.type_login()
