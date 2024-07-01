from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://192.168.46.5:14753/login')
driver.find_element(By.NAME, 'username').send_keys("XTGLY")
driver.find_element(By.NAME, 'password').send_keys('123456')
sleep(1)
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, '客户信息').click()

d_elem = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/button[1]')
driver.execute_script('arguments[0].removeAttribute(\"style\")', d_elem)
# 删除第一个查看的style属性
elem = driver.find_elements(By.LINK_TEXT, '查看')[0]
driver.execute_script('arguments[0].removeAttribute(\"target\")', elem)
# 移出target属性
sleep(1)
elem.click()
sleep(2)
driver.get_screenshot_as_file('./test_target01.png')
driver.find_element(By.CLASS_NAME,'el-dialog__close').click()
