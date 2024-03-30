import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class ERP_T2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.find_element(By.NAME, "username").send_keys("XTGLY")
        self.driver.find_elements(By.CLASS_NAME, "password")[0].send_keys("123456")
        self.driver.find_element(By.XPATH, '//*[@id=\"signIn\"]').click()

    def test_denglu02(self):
        self.driver.find_element(By.ID, "username").send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME, "password").send_keys("123456")
        self.driver.find_element(By.TAG_NAME, "button").click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, "供应商信息").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button[1]/span/a").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/button/i").click()


if __name__ == '__main__':
    unittest.main()
