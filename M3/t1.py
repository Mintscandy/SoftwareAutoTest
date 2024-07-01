from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://192.168.46.5:14753/login')

driver.find_element(By.NAME, 'username').send_keys("XTGLY")
driver.find_element(By.ID, 'password').send_keys("123456")
driver.find_element(By.TAG_NAME, 'button').click()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, '商品品牌').click()
sleep(1)
driver.find_elements(By.TAG_NAME, 'button')[5].click()
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]').click()
