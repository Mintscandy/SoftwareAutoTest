from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import ddt


@ddt.ddt()
class T3(unittest.TestCase):
    import csvv
    case_data = csvv.read_csv("testdata.csv")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @ddt.data(*case_data)
    def test_01(self, data):
        self.driver.get("http://192.168.46.5:14753")
        self.driver.find_element(By.CLASS_NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.TAG_NAME, "button").click()
        sleep(1)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "商品品牌").click()
        sleep(1)
        self.driver.find_elements(By.TAG_NAME, "button")[3].click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys(data[0])
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]").click()
        sleep(1)

        text = self.driver.find_element(By.CLASS_NAME, "el-form-item__error").text
        try:
            self.assertEqual(text, data[1])
        except BaseException as e:
            self.driver.get_screenshot_as_file("test03.png")


if __name__ == '__main__':
    unittest.main()
