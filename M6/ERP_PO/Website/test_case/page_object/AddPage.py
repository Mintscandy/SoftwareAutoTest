from selenium.common import NoSuchElementException

from M6.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By
from time import sleep


class Add(Page):
    cateorgy_loc = (By.PARTIAL_LINK_TEXT, '商品分类')
    add_loc = (By.CSS_SELECTOR, '#app > div > div.main-container.hasTagsView > section > div > div.mb8.el-row > '
                                'div:nth-child(3) > button')
    name_loc = (By.XPATH, '/html/body/div[2]/div/div[2]/form/div/div/div[1]/div/input')
    save_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > '
                                 'button.el-button.el-button--primary.el-button--medium')
    error_loc = (By.CLASS_NAME, 'el-form-item__error')
    correct_loc = (By.CLASS_NAME, 'el-message__content')

    def type_cateorgy(self):
        self.find_element(*self.cateorgy_loc).click()

    def type_add(self):
        self.find_element(*self.add_loc).click()

    def type_name(self, name):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.name_loc).send_keys(name)

    def type_save(self):
        self.find_element(*self.save_loc).click()

    def get_alert(self):
        sleep(3)
        try:
            em = self.find_element(*self.error_loc).text
            pass
            return em
        except NoSuchElementException as e:
            em = self.find_element(*self.correct_loc).text
            pass
            return em


def test_add_page(driver, name):
    add_page = Add(driver)
    add_page.type_cateorgy()
    sleep(1)
    add_page.type_add()
    sleep(1)
    add_page.type_name(name)
    sleep(1)
    add_page.type_save()
