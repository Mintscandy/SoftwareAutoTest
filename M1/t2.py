import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import unittest
import ddt

class ERP_T(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.46.5:14753/login')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_denglu01(self):
        self.driver.find_element(By.NAME,'username').send_keys("XTGLY")
        self.driver.find_element(By.NAME,'password').send_keys("123456")
        self.driver.find_element(By.ID,'signIn').click()
        sleep(1)

    def test_denglu02(self):
        self.driver.find_element(By.NAME,'username').send_keys("XTGLY")
        self.driver.find_element(By.ID,'password').send_keys("123456")
        self.driver.find_element(By.TAG_NAME,'button').click()
        sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/section/div/div[2]/div[3]/button').click()
        file = r'/Users/zhudichuan/Downloads/软件测试/基于Python/实训18 Selenium之文件上传处理.pdf'
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/form/div[7]/div/div/div/div').send_keys(file)
        sleep(3)


