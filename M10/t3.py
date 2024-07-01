from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import unittest
import ddt


@ddt.ddt()
class ERPT1(unittest.TestCase):
    import csvv
    cd = csvv.read(".testdata.csv")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @ddt.data(*cd)
    def test_denglu01(self, l):
        self.driver.get('http://192.168.46.5:14753/')
        self.driver.find_element(By.ID, "username").send_keys("XTGLY")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.TAG_NAME, "button").click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, "商品分类").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/section/div/div[2]/div[3]/button").click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys(l[0])
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/button[1]').click()
        elem = self.driver.find_element(By.CLASS_NAME, 'el-form-item__error').text
        self.assertEqual(elem, l[1])


if __name__ == '__main__':
    unittest.main()
