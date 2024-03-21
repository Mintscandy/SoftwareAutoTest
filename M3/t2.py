from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class ERP1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('http://192.168.46.5:16209/login')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.NAME, 'username').send_keys("XTGLY")
        self.driver.find_element(By.NAME, 'password').send_keys("123456")
        self.driver.find_element(By.XPATH, '/html/body/div/div/form/div[4]/div/button').click()

    def test_denglu02(self):
        self.driver.find_element(By.NAME, 'username').send_keys("XTGLY")
        self.driver.find_element(By.ID, 'password').send_keys('123456')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, '客户信息').click()
        elem = self.driver.find_element(By.XPATH,
                                        '/html/body/div/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button[1]')
        self.driver.execute_script('arguments[0].removeAttribute(\"style\")', elem)
        sleep(1)
        target = self.driver.find_elements(By.LINK_TEXT, '查看')[0]
        self.driver.execute_script('arguments[0].removeAttribute(\"target\")', target)
        sleep(1)
        target.click()
        self.driver.get_screenshot_as_file("target.png")


if __name__ == "__main__":
    unittest.main()
