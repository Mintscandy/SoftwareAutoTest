import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


@ddt.ddt()
class T3(unittest.TestCase):
    import csvv
    dc = csvv.readcsv("testdata.csv")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @ddt.data(*dc)
    def test01(self, l):
        self.driver.get('http://192.168.46.5:16209/')
        self.driver.find_elements(By.TAG_NAME, "input")[0].send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, 'signIn').click()
        sleep(1)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "商品分类").click()
        sleep(1)
        self.driver.find_elements(By.TAG_NAME, "button")[3].click()
        self.driver.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > "
                                                  "div > div > div.el-col.el-col-16 > div > input").send_keys(l[0])
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/button[1]').click()
        elem = self.driver.find_element(By.CLASS_NAME, 'el-form-item__error').text
        try:
            self.assertEqual(elem, l[1])
        except BaseException as e:
            self.driver.get_screenshot_as_file("t3.png")


if __name__ == '__main__':
    unittest.main()
