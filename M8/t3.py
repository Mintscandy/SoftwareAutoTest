import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import ddt


@ddt.ddt()
class ERP(unittest.TestCase):
    import csvv
    case_data = csvv.read("testdata.csv")
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
    @ddt.data(*case_data)
    def test_01(self,l):
        self.driver.get('http://192.168.46.5:14753/')
        self.driver.find_element(By.NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME, "password").send_keys("123456")
        self.driver.find_element(By.ID, "signIn").click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT,"商品单位").click()
        sleep(1)
        self.driver.find_elements(By.TAG_NAME,"button")[3].click()
        self.driver.find_element(By.CLASS_NAME,"el-input__inner").send_keys(l[0])
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[1]').click()
        elem = self.driver.find_element(By.CLASS_NAME,'el-form-item__error').text
        try:
            self.assertEqual(elem,l[1])
        except BaseException as e:
            self.driver.get_screenshot_as_file("a.png")

if __name__ == '__main__':
    unittest.main()





if __name__ == '__main__':
    unittest.main()
