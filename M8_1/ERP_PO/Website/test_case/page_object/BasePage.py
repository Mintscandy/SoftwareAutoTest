from selenium import webdriver
class Page:
    def __init__(self, driver):
        self.driver= driver
        self.base_url = 'http://192.168.46.5:14753'
        self.timeout = 10

    def _open(self, url):
        # 这里这么写是有道理的哦~
        # 俺知道 只不过觉得太繁琐了
        # 是哒 但是理解了就觉得还是蛮简单的
        _url = self.base_url + url
        self.driver.get(_url)

    def open(self):
        return self._open(self.url)
    # 用下面这个叭
    # def OpenUrl(self):
    #     self.driver.get(self.base_url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
