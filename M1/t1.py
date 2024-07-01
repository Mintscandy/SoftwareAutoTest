from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://192.168.46.5:14753/login')
driver.find_element(By.NAME, 'username').send_keys("XTGLY")
driver.find_element(By.ID, 'password').send_keys("123456")
sleep(1)
driver.find_element(By.TAG_NAME, 'button').click()
sleep(2)
driver.find_element(By.LINK_TEXT, '仓库信息').click()
sleep(1)
driver.find_elements(By.TAG_NAME, 'button')[5].click()
sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/button/i').click()
