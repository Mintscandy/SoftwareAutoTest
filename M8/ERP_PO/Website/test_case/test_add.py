from selenium import webdriver
from M8.ERP_PO.Website.test_case.model import myunit, function
from M8.ERP_PO.Website.test_case.page_object.LoginPage import *
from M8.ERP_PO.Website.test_case.page_object.BasePage import *
from M8.ERP_PO.Website.test_case.page_object.AddPage import *
import time
import ddt


@ddt.ddt()
class final(myunit.StartEnd):
    user = ["XTGLY", "123456"]
    data_path = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M8\ERP_PO\Website\test_data\test_csv.csv'

    def test_01(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 0)
        test_add_page(self.driver, data[0])
        now = time.strftime("%H_%M_%S")
        function.inser_img(self.driver, "test" + now + ".png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test_02(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 1)
        test_add_page(self.driver, data[0])
        now = time.strftime("%H_%M_%S")
        function.inser_img(self.driver, "test" + now + ".png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test_03(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 2)
        test_add_page(self.driver, data[0])
        now = time.strftime("%H_%M_%S")
        function.inser_img(self.driver, "test" + now + ".png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test_04(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 3)
        test_add_page(self.driver, data[0])
        now = time.strftime("%H_%M_%S")
        function.inser_img(self.driver, "test" + now + ".png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test_05(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_path, 4)
        test_add_page(self.driver, data[0])
        now = time.strftime("%H_%M_%S")
        function.inser_img(self.driver, "test" + now + ".png")
        self.assertIn(Add(self.driver).get_alert(), data[1])
