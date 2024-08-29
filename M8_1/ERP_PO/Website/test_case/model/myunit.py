import unittest
from M8_1.ERP_PO.driver.driver import *
class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def tearDown(self) -> None:
        self.driver.quit()
# 不要留空格哦，不然你文档上会很难看