import time
from time import sleep
from M1.EPR_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    url = "/login"
    username_loc = (By.ID, "username")
    password_loc = (By.NAME, 'password')
    submit_loc = (By.CLASS_NAME, 'el-button--medium')

    def type_username(self, username):
        # 访问的是BasePage的find_element
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    sleep(2)
    login_page = LoginPage(driver)
    # 这里是直接返回了_open
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()
