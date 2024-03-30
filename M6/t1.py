from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://192.168.46.5:16209/')
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.NAME, 'username').send_keys("XTGLY")
driver.find_element(By.ID, 'password').send_keys("123456")
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(2)
driver.find_elements(By.TAG_NAME, 'button')[3].click()
sleep(1)

select = driver.find_element(By.CSS_SELECTOR, '#select_add_brand_bug')
Select(select).select_by_visible_text("品牌")
