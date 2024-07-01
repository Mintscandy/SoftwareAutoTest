from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://192.168.46.5:14753/')
driver.maximize_window()
driver.find_element(By.ID, 'username').send_keys("XTGLY")
driver.find_element(By.NAME, 'password').send_keys("123456")
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(2)
driver.find_elements(By.TAG_NAME, 'button')[3].click()
sleep(8)
elem = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M4\t1.py"
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/form/div[7]/div/div/div/div').send_keys(elem)
driver.get_screenshot_as_file(r"D:\\test_picture.png")
