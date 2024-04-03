from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get('http://192.168.46.5:16209/')
driver.find_element(By.ID, "username").send_keys("XTGLY")
driver.find_elements(By.TAG_NAME, "input")[1].send_keys("123456")
driver.find_element(By.CLASS_NAME, "signIn").click()
sleep(1)
driver.find_elements(By.TAG_NAME, "button")[3].click()
sleep(1)
elem = driver.find_element(By.ID, 'select_add_class_bug')
Select(elem).select_by_value("2")
elems = driver.find_elements(By.TAG_NAME, "input")[3]
Select(elems).select_by_index("测试")
driver.get_screenshot_as_file("D:\\test_Select01.png")