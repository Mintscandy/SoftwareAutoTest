from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://192.168.46.5:14753/')
driver.find_element(By.NAME, "username").send_keys("XTGLY")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "el-button").click()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "供应商信息").click()
sleep(1)
driver.find_elements(By.LINK_TEXT, "查看")[0].click()
driver.switch_to.window(driver.window_handles[-1])
sleep(3)
driver.get_screenshot_as_file("D:\\test_handles.png")
driver.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__header > button > i").click()
