from time import sleep

from PoTest.Page.LoginPage import *
from PoTest.Page.AddPage import *
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

test_login_page(driver,"XTGLY","123456")
sleep(3)
test_add_page(driver,"测试")
sleep(3)
driver.quit()