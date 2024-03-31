import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from M10.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class AddPage(Page):
    pp_loc = (By.LINK_TEXT, "商品品牌",)
    add_loc = (By.XPATH, "/html/body/div/div/div[2]/section/div/div[2]/div[3]/button",)
    name_loc = (By.XPATH, '/html/body/div[2]/div/div[2]/form/div/div/div[1]/div/input',)
    save_loc = (By.CSS_SELECTOR,
                "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium",)
    error_loc = (By.CLASS_NAME, 'el-form-item__error')
    correct_loc = (By.CLASS_NAME, 'el-message__content',)

    def type_pp(self):
        self.find_element(*self.pp_loc).click()

    def type_add(self):
        self.find_element(*self.add_loc).click()

    def type_name(self, name):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.name_loc).send_keys(name)

    def type_save(self):
        self.find_element(*self.save_loc).click()

    def get_alert(self):
        time.sleep(3)
        try:
            et = self.find_element(*self.error_loc).text
            pass
            return et
        except NoSuchElementException as e:
            et = self.find_element(*self.correct_loc).text
            return et


def test_add_page(driver, name):
    add = AddPage(driver)
    add.type_pp()
    time.sleep(1)
    add.type_add()
    time.sleep(1)
    add.type_name(name)
    time.sleep(1)
    add.type_save()
