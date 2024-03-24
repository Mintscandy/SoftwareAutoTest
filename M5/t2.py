import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class T2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.46.5:16209')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.CLASS_NAME, "username").send_keys("XTGLY")
        self.driver.find_elements(By.TAG_NAME, "input")[1].send_keys("123456")
        self.driver.find_element(By.ID, "signIn").click()

    def test_denglu02(self):
        self.driver.find_element(By.CLASS_NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.ID, 'password').send_keys("123456")
        self.driver.find_element(By.TAG_NAME, "button").click()
        sleep(1)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '仓库信息').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr['
                                           '1]/td[9]/div/button[2]').click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'el-message-box__close').click()
