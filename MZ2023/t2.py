from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class T2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.find_element(By.CLASS_NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.XPATH, '/html/body/div/div/form/div[4]/div/button').click()

    def test_denglu02(self):
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.find_element(By.NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
        self.driver.find_element(By.TAG_NAME, "button").click()
        sleep(1)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "供应商信息").click()
        sleep(1)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button[1]/span/a").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.el-dialog__wrapper > div > div.el-dialog__header > button > i").click()
        self.driver.get_screenshot_as_file("test_02.png")


if __name__ == '__main__':
    unittest.main()
