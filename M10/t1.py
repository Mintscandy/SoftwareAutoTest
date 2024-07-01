import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://192.168.46.5:14753/')
driver.find_element(By.NAME, "username").send_keys("XTGLY")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)
driver.find_element(By.XPATH,
                    "/html/body/div/div/div[2]/section/div/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[13]/div/button[2]").click()
driver.switch_to.alert.accept()
time.sleep(1)
driver.get_screenshot_as_file("D:\\test_accept01.png")
