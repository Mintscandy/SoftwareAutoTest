from selenium import webdriver
from selenium.webdriver.common.by import By
# 为啥你喜欢用这个sleep啊 啊哈哈哈
# 因为这样的话就可以直接sleep(2) 不然还要time.sleep(2)这样 好好好
from time import sleep
driver = webdriver.Chrome()
driver.get("http://192.168.46.5:14753/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("XTGLY")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.TAG_NAME, "button").click()
driver.find_element(By.LINK_TEXT, "供应商信息").click()
sleep(2)
driver.find_elements(By.LINK_TEXT, "查看")[0].click()
sleep(1)
# 这里可以是driver.window_handles[-1]，因为在测试环境中，没有其他的页面打开，-1表示逆向索引 表示最新打开的那个
# 懂啦，其实这个地方题目有问题的，英文你点查看后，它自己就切换到那个页面了
# 不是哒，那个是bug，是自动化的bug
# 不是可以导出来Bug列表么，你可以看最后几条 大概是70几开始，就是自动化的Bug啦
# 自动化bug一共有13还是14来着，唔那个自动化bug是故意设计的bug，就是要做自动化的题，就必须开这些bug的：嗯嗯 我知道 继续吧
driver.switch_to.window(driver.window_handles[1])
sleep(3)
driver.get_screenshot_as_file("D:\\test_handles.png")
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button').click()
