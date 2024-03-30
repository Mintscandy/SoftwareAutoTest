from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import unittest

class ERP_T(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.find_element(By.NAME,"username").send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME,"password").send_keys("123456")
        self.driver.find_element(By.XPATH,'/html/body/div/div/form/div[4]/div/button').click()

    def test_denglu02(self):
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.find_element(By.ID,"username").send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME,'password').send_keys("123456")
        self.driver.find_element(By.TAG_NAME,"button").click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT,"供应商信息").click()
        sleep(1)
        self.driver.find_elements(By.TAG_NAME,"button")[7].click()


if __name__ == '__main__':
    unittest.main()