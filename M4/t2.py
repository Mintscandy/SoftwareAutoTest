from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest


class M4(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.46.5:14753/')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_elements(By.TAG_NAME, 'input')[0].send_keys("XTGLY")
        self.driver.find_elements(By.TAG_NAME, 'input')[1].send_keys("123456")
        self.driver.find_element(By.CLASS_NAME, 'el-button').click()

    def test_denglu02(self):
        self.driver.find_element(By.CLASS_NAME, 'username').send_keys("XTGLY")
        self.driver.find_element(By.NAME, 'password').send_keys("123456")
        self.driver.find_element(By.ID, 'signIn').click()
        sleep(2)
        elem = Select(self.driver.find_element(By.ID, 'select_query_class'))
        elem.select_by_value("测试")


if __name__ == '__main__':
    unittest.main()
