from selenium.common import NoSuchElementException

from M1.EPR_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By
from time import sleep


class Add(Page):
    Brand_loc = (By.LINK_TEXT, '商品品牌')
    Add_loc = (By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div[2]/div[3]/button')
    Name_loc = (By.XPATH, '/html/body/div[2]/div/div[2]/form/div/div/div[1]/div/input')
    Save_loc = (By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
    error_loc = (By.CLASS_NAME, 'el-form-item__error')
    correct_loc = (By.CLASS_NAME, 'el-message__content')

    def type_brand(self):
        self.find_element(*self.Brand_loc).click()

    def type_add(self):
        self.find_element(*self.Add_loc).click()

    def type_name(self, name):
        self.find_element(*self.Name_loc).clear()
        self.find_element(*self.Name_loc).send_keys(name)

    def type_baocun(self):
        self.find_element(*self.Save_loc).click()

    def get_alert(self):
        sleep(2)
        try:
            et = self.find_element(*self.error_loc).text
            pass
            return et
        except NoSuchElementException as e:
            print("捕获异常")
            et = self.find_element(*self.correct_loc).text
            return et


def test_brand_add(driver, name):
    add_page = Add(driver)
    add_page.type_brand()
    sleep(1)
    add_page.type_add()
    sleep(3)
    add_page.type_name(name)
    sleep(1)
    add_page.type_baocun()
