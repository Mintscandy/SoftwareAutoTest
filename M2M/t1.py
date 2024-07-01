from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://192.168.46.5:14753/")
driver.find_element(By.NAME, "username").send_keys("XTGLY")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "el-button").click()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "客户信息").click()
elem = driver.find_elements(By.LINK_TEXT, "查看")[0]
driver.execute_script("arguments[0].removeAttribute(\"target\")", elem)
elem.click()
sleep(2)
driver.get_screenshot_as_file("D:\\test_target01.png")
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/button").click()
