from selenium import webdriver
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from M4.ERP_PO.Website.test_case.page_object.BasePage import *


class AddPage(Page):
    brand_loc = (By.LINK_TEXT, "商品品牌")
    add_loc = (By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[2]/div[3]/button")
    name_loc = (By.XPATH, '/html/body/div[2]/div/div[2]/form/div/div/div[1]/div/input')
    submit_loc = (By.CSS_SELECTOR,
                  'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
    error_loc = (By.CLASS_NAME, 'el-form-item__error')
    correct_loc = (By.CLASS_NAME, 'el-message__content')

    def type_brand(self):
        self.find_element(*self.brand_loc).click()

    def type_add(self):
        self.find_element(*self.add_loc).click()

    def type_name(self, name):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.name_loc).send_keys(name)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def get_alert(self):
        sleep(5)
        try:
            el = self.find_element(*self.error_loc).text
            pass
            return el
        except NoSuchElementException as e:
            sleep(3)
            el = self.find_element(*self.correct_loc).text
            return el


def test_add_page(driver, name):
    add_page = AddPage(driver)

    add_page.type_brand()
    sleep(1)
    add_page.type_add()
    sleep(1)
    add_page.type_name(name)
    sleep(1)
    add_page.type_submit()
