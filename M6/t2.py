from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class T1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://192.168.46.5:16209/')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.NAME,"username").send_keys("XTGLY")
        self.driver.find_element(By.ID,'password').send_keys("123456")
        self.driver.find_element(By.CLASS_NAME,"el-button").click()

    def test_denglu02(self):
        self.driver.find_element(By.NAME,'username').send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME,"password").send_keys("123456")
        self.driver.find_element(By.ID,"signIn").click()
        sleep(1)
        elem = self.driver.find_element(By.NAME,'select_brand_bug')
        Select(elem).select_by_visible_text("测试")

if __name__ == '__main__':
    unittest.main()
