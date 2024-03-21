import unittest
from M2.ERP_PO.driver.driver import browser


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
