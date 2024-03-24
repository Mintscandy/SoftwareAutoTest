from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import unittest
import ddt


@ddt.ddt()
class ERP02(unittest.TestCase):
    import csvv
    case_data = csvv.readfile("testdata.csv")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @ddt.data(*case_data)
    def test_first(self, l):
        self.driver.find_element(By.CLASS_NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.TAG_NAME, "TAG_NAME").click()
        sleep(1)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '商品品牌').click()
        self.driver.find_elements(By.TAG_NAME, "button")[3].click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys(l[0])
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/button[1]').click()
        elem = self.driver.find_element(By.CLASS_NAME, 'el-form-item__error').text
        self.assertEqual(elem, l[1])


if __name__ == '__main__':
    unittest.main()
