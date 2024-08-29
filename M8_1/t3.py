import time
from csvv import read_csv
from M8_1.csvv import read_csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import ddt
@ddt.ddt
class T3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.46.5:14753/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.quit()
    #     你这个括号里面写的有点复杂了吧
    # @ddt.data(*read_csv())
    # 这里是要传路径的，因为我read_csv方法里没有把路径写死
    @ddt.data(*read_csv(r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M8_1\testdata.csv"))
    def test_01(self, l):
        self.driver.find_element(By.NAME, "username").send_keys("XTGLY")
        self.driver.find_element(By.CLASS_NAME, "password").send_keys("123456")
        self.driver.find_element(By.ID, 'signIn').click()
        self.driver.find_element(By.LINK_TEXT, "商品单位").click()
        time.sleep(2)
        self.driver.find_elements(By.TAG_NAME, "button")[3].click()
        time.sleep(5)
        # 知道为什么这个地方要加这个吗？ 不知道诶
        self.driver.find_elements(By.CLASS_NAME, "el-input__inner")[4].send_keys(l[0])
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button/span[text()='保存']").click()
        time.sleep(2)
        text = self.driver.find_element(By.CLASS_NAME, 'el-form-item__error').text
        try:
            self.assertEqual(l[1], text)
        except AssertionError:
            self.driver.get_screenshot_as_file("D:\\error.png")
if __name__ == '__main__':
    unittest.main()