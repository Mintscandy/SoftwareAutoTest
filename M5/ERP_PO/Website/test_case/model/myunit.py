import unittest
from M5.ERP_PO.driver.driver import browser


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.quit()
