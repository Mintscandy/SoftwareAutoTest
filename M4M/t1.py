from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://192.168.46.5:14753")
driver.find_element(By.ID, "username").send_keys("XTGLY")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "el-button").click()
sleep(2)
driver.find_elements(By.TAG_NAME, "button")[3].click()
sleep(1)
img = r"C:\Users\Mints_Candy\Pictures\Screenshots\屏幕截图 2024-03-27 103544.png"
driver.find_element(By.NAME, "file").send_keys(img)
driver.get_screenshot_as_file("D:\\test_picture.png")
