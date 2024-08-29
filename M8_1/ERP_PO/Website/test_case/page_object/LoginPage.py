from M8_1.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By
import time


class LoginPage(Page):
    url = '/login'
    username_loc = (By.CLASS_NAME, "username")
    password_loc = (By.ID, "password")
    login_btn_loc = (By.TAG_NAME, "button")

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_login(self):
        self.find_element(*self.login_btn_loc).click()
#         教你你个快捷键，一键调整格式 1.先全选 2.ctrl+alt+L  你试试
def test_login_page(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login()
    time.sleep(2)
#     这个地方用不到sleep，因为你前面写了智能等待，这个属于只能等待时间
# 下次用time.sleep（）
