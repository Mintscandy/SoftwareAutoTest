from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://192.168.46.5:14753/')
driver.find_element(By.ID, 'username').send_keys("XTGLY")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.TAG_NAME, "button").click()
sleep(1)
driver.find_element(By.LINK_TEXT, "供应商信息").click()
sleep(1)
driver.find_elements(By.LINK_TEXT, "查看")[0].click()
driver.switch_to.window(driver.window_handles[-1])
sleep(3)
driver.get_screenshot_as_file("D:\\test_handles.png")
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button').click()
