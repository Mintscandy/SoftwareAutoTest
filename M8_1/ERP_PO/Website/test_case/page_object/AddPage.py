import time

from selenium.common import NoSuchElementException

from M8_1.ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By
from time import sleep


class AddPage(Page):
    unit_loc = (By.LINK_TEXT, "商品单位",)
    add_loc = (By.XPATH, "//button/span[text()='新增']")
    unit_name_loc = (By.XPATH, '//input[@*="请输入商品单位名称"]')
    save_loc = (By.CSS_SELECTOR,
                'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
    success_loc = (By.CLASS_NAME, "el-form-item__error")
    error_loc = (By.CLASS_NAME, 'el-message__content')

    def type_unit(self):
        self.find_element(*self.unit_loc).click()

    def type_add(self):
        self.find_element(*self.add_loc).click()

    def type_unit_name(self, unit_name):
        self.find_element(*self.unit_name_loc).clear()
        self.find_element(*self.unit_name_loc).send_keys(unit_name)

    def type_save(self):
        self.find_element(*self.save_loc).click()

    # 这个地方 判断有点多余哦
    # 你昨天跟我解释过啦
    # 好嘟
    def get_alert(self):
        sleep(3)
        try:
            et = self.find_element(*self.error_loc).text
            return et
            pass
        except NoSuchElementException as e:
            et = self.find_element(*self.success_loc).text
            return et
            pass


def test_add_page(driver, unit_name):
    add_page = AddPage(driver)
    # 这个也是属于智能等待的，就是你点击左侧商品单位之后才需要time.sleep（2）
    sleep(2)
    add_page.type_unit()
    sleep(2)
    add_page.type_add()
    sleep(2)
    add_page.type_unit_name(unit_name)
    sleep(2)
    add_page.type_save()
    time.sleep(2)
#     这个地方需要一个等待时间哦，它把正确错误的文字返回出来
