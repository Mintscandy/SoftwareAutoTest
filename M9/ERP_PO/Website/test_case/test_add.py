import time

from M9.ERP_PO.Website.test_case.page_object.AddPage import *
from M9.ERP_PO.Website.test_case.page_object.BasePage import *
from M9.ERP_PO.Website.test_case.page_object.LoginPage import *
from M9.ERP_PO.Website.test_case.model import myunit, function
import unittest
import ddt

@ddt.ddt()
class final(myunit.StartEnd):
    user = ["XTGLY", "123456"]
    dp = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M9\ERP_PO\Website\test_data\test_csv.csv"

    def test_01(self):
        test_login_page(self.driver, self.user[0], self.user[1])

        data = function.get_csv_line(self.dp, 1)
        test_add_page(self.driver, data[0])
        in_path = str(time.time())
        function.inser_img(self.driver, in_path)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_02(self):
        test_login_page(self.driver, self.user[0], self.user[1])

        data = function.get_csv_line(self.dp, 2)
        test_add_page(self.driver, data[0])
        in_path = str(time.time())
        function.inser_img(self.driver, in_path)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_03(self):
        test_login_page(self.driver, self.user[0], self.user[1])

        data = function.get_csv_line(self.dp, 2)
        test_add_page(self.driver, data[0])
        in_path = str(time.time())
        function.inser_img(self.driver, in_path)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_04(self):
        test_login_page(self.driver, self.user[0], self.user[1])

        data = function.get_csv_line(self.dp, 3)
        test_add_page(self.driver, data[0])
        in_path = str(time.time())
        function.inser_img(self.driver, in_path)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_05(self):
        test_login_page(self.driver, self.user[0], self.user[1])

        data = function.get_csv_line(self.dp, 4)
        test_add_page(self.driver, data[0])
        in_path = str(time.time())
        function.inser_img(self.driver, in_path)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

