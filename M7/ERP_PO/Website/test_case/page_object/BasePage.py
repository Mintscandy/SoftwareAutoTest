from selenium import webdriver
from time import sleep


class Page():
    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver.Chrome = driver
        self.base_url = 'http://192.168.46.5:14753'

    def _open(self, url):
        url_ = self.base_url + url
        self.driver.get(url_)

    def open(self):
        return self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)