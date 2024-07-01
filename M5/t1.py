from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://192.168.46.5:14753')
driver.find_element(By.NAME, "username").send_keys("系统管理员")
driver.find_element(By.ID, '123456').send_keys("123456")
driver.find_element(By.TAG_NAME, 'button').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#select_query_class')
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[16]').click()
driver.get_screenshot_as_file("D:\\test_Select01.png")

