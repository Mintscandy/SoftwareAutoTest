import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class T2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get('http://192.168.46.5:14753/login')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.ID, 'username').send_keys("XTGLY")
        self.driver.find_element(By.NAME, 'password').send_keys("123456")
        self.driver.find_element(By.TAG_NAME, 'button').click()

    def test_denglu02(self):
        self.driver.find_element(By.NAME, 'username').send_keys("XTGLY")
        self.driver.find_element(By.ID, 'password').send_keys("123456")
        self.driver.find_element(By.CLASS_NAME, 'el-button').click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, '客户信息').click()


if __name__ == "__main__":
    unittest.main()
