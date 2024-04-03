from selenium import webdriver
import unittest
import time
import ddt
from MZ2023.EPR_PO.Webisite.test_case.page_object.AddPage import *
from MZ2023.EPR_PO.Webisite.test_case.page_object.LogingPage import *
from MZ2023.EPR_PO.Webisite.test_case.model import myunit, function


@ddt.ddt()
class final(myunit.StartEnd):
    user = ["XTGLY", "123456"]
    data_path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\MZ2023\EPR_PO\Webisite\test_data\test_csv.csv"

    def test_01(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 0)
        test_add_page(self.driver, data[0])
        png = str(time.strftime("%H_%M_%S"))
        function.inser_img(self.driver,"test_" + png + ".png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_02(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 1)
        test_add_page(self.driver, data[0])
        png = str(time.strftime("%H_%M_%S"))
        function.inser_img(self.driver,"test_" + png + ".png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_03(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 2)
        test_add_page(self.driver, data[0])
        png = str(time.strftime("%H_%M_%S"))
        function.inser_img(self.driver,"test_" + png + ".png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_04(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 3)
        test_add_page(self.driver, data[0])
        png = str(time.strftime("%H_%M_%S"))
        function.inser_img(self.driver,"test_" + png + ".png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_05(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 4)
        test_add_page(self.driver, data[0])
        png = str(time.strftime("%H_%M_%S"))
        function.inser_img(self.driver,"test_" + png + ".png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test_06(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 5)
        test_add_page(self.driver, data[0])
        png = str(time.strftime("%H_%M_%S"))
        function.inser_img(self.driver,"test_" + png + ".png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1])
