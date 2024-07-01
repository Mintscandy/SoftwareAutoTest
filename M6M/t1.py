from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://192.168.46.5:14753")
driver.find_element(By.NAME, "username").send_keys("XTGLY")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "el-button").click()
sleep(1)
driver.find_elements(By.TAG_NAME, "button")[3].click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="select_class_bug"]/option[3]').click()
elem = driver.find_element(By.CSS_SELECTOR, "#select_brand_bug")
select = Select(elem)
select.select_by_visible_text("测试")
driver.get_screenshot_as_file("D:\\test_Select01.png")
