from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://192.168.46.5:16209/')
driver.find_element(By.ID, "username").send_keys("XTGLY")
driver.find_element(By.NAME, 'password').send_keys("123456")
login_button = driver.find_element(By.TAG_NAME, "button")

ActionChains(driver).click(login_button).perform()
sleep(1)
product_name = driver.find_element(By.ID, 'product_name')
product_name.send_keys("test01")
ActionChains(driver).double_click(product_name).perform()

driver.get_screenshot_as_file("D:\\test_ActionChains01.png")