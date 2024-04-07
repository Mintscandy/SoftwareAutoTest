from selenium import webdriver

class Page():
    def __init__(self,driver):
        self.driver:webdriver.Chrome = driver
        self.base_url = "http://192.168.46.5:16209"
    def _open(self,url):
        self.driver.get(self.base_url + url)
    def open(self):
        return self._open(self.url)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)