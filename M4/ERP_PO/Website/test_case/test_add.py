from selenium import webdriver
import unittest
import ddt
from M4.ERP_PO.Website.test_case.model import function, myunit
from M4.ERP_PO.Website.test_case.page_object.AddPage import *
from M4.ERP_PO.Website.test_case.page_object.LoginPage import *
from M4.ERP_PO.Website.test_case.page_object.BasePage import *

@ddt.ddt()
class ERP(myunit.StartEnd):
    user_info = ['XTGLY', '123456']

    datapath = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M4\ERP_PO\Website\test_data\testdata.csv'

    def test_01(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_line(self.datapath, 0)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, "test01.png")
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())

    def test_02(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_line(self.datapath, 1)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, "test02.png")
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())

    def test_03(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_line(self.datapath, 2)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, "test03.png")
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())

    def test_04(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_line(self.datapath, 3)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, "test04.png")
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())

    def test_05(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_line(self.datapath, 4)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, "test05.png")
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())

    def test_06(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_line(self.datapath, 5)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, "test06.png")
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
