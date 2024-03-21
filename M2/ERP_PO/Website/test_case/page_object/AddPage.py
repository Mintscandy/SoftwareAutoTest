import time
from time import sleep

from selenium.common import NoSuchElementException

from M2.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class AddPage(Page):
    Category_loc = (By.PARTIAL_LINK_TEXT, '商品分类')
    Add_loc = (By.CSS_SELECTOR,
               '#app > div > div.main-container.hasTagsView > section > div > div.mb8.el-row > div:nth-child(3) > button')
    Name_loc = (By.XPATH, '/html/body/div[2]/div/div[2]/form/div/div/div[1]/div/input')
    Save_loc = (By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
    error_loc = (By.CLASS_NAME, 'el-form-item__error')
    correct_loc = (By.CLASS_NAME, 'el-message__content')

    def type_category(self):
        self.find_element(*self.Category_loc).click()

    def type_add(self):
        self.find_element(*self.Add_loc).click()

    def type_name(self, name):
        self.find_element(*self.Name_loc).clear()
        self.find_element(*self.Name_loc).send_keys(name)

    def type_save(self):
        self.find_element(*self.Save_loc).click()

    def get_alert(self):
        sleep(5)
        try:
            et = self.find_element(*self.error_loc).text
            pass
            return et
        except NoSuchElementException as e:
            sleep(3)
            et = self.find_element(*self.correct_loc).text
            return et


def test_category_add(driver, name):
    add_page = AddPage(driver)
    add_page.type_category()
    sleep(1)
    add_page.type_add()
    sleep(3)
    add_page.type_name(name)
    sleep(1)
    add_page.type_save()
