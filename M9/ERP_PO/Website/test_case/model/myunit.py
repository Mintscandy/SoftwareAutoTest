import unittest
from M9.ERP_PO.driver.driver import *


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = broswer()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
