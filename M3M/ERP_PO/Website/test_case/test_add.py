import unittest
import ddt
import time
from M3M.ERP_PO.Website.test_case.model import function, myunit
from M3M.ERP_PO.Website.test_case.page_object.BasePage import *
from M3M.ERP_PO.Website.test_case.page_object.LogingPage import *
from M3M.ERP_PO.Website.test_case.page_object.AddPage import *


@ddt.ddt()
class final(myunit.StartEnd):
    user = ["XTGLY", "123456"]
    data_path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M3M\ERP_PO\Website\test_data\test_csv.csv"

    def test01(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 0)
        test_add_page(self.driver, data[0])
        pm = "test_" + str(time.strftime("%H_%M_%S")) + ".png"
        function.inser_img(self.driver, pm)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test02(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 1)
        test_add_page(self.driver, data[0])
        pm = "test_" + str(time.strftime("%H_%M_%S")) + ".png"
        function.inser_img(self.driver, pm)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test03(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 2)
        test_add_page(self.driver, data[0])
        pm = "test_" + str(time.strftime("%H_%M_%S")) + ".png"
        function.inser_img(self.driver, pm)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test04(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 3)
        test_add_page(self.driver, data[0])
        pm = "test_" + str(time.strftime("%H_%M_%S")) + ".png"
        function.inser_img(self.driver, pm)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test05(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 4)
        test_add_page(self.driver, data[0])
        pm = "test_" + str(time.strftime("%H_%M_%S")) + ".png"
        function.inser_img(self.driver, pm)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test06(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 5)
        test_add_page(self.driver, data[0])
        pm = "test_" + str(time.strftime("%H_%M_%S")) + ".png"
        function.inser_img(self.driver, pm)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])
