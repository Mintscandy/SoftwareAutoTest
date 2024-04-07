from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import unittest

class T2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.get("http://192.168.46.5:16209")
        self.driver.find_element(By.NAME,"username").send_keys("XTGLY")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.XPATH,'//*[@id="signIn"]').click()

    def test_denglu02(self):
        self.driver.get("http://192.168.46.5:16209")
        self.driver.find_element(By.NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.TAG_NAME,"button").click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT,"客户信息").click()
        sleep(1)
        elem = self.driver.find_elements(By.LINK_TEXT,"查看")[0]
        self.driver.execute_script("arguments[0].removeAttribute(\"target\")",elem)
        elem.click()
        self.driver.get_screenshot_as_file("test02.png")

if __name__ == '__main__':
    unittest.main()




