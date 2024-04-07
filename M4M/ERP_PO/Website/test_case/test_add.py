import ddt
import unittest
import time
from M4M.ERP_PO.Website.test_case.model import myunit,function
from M4M.ERP_PO.Website.test_case.page_object.AddPage import *
from M4M.ERP_PO.Website.test_case.page_object.LogingPage import *
@ddt.ddt()
class final(myunit.StartEnd):
    user = ["XTGLY","123456"]
    data_path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M4M\ERP_PO\Website\test_data\test_csv.csv"
    def test_01(self):
        test_login_page(self.driver,self.user[0],self.user[1])
        data = function.get_csv_line(self.data_path,0)
        test_add_page(self.driver,data[0])
        png = "test_" + time.strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,png)
        self.assertIn(AddPage(self.driver).get_alert(),data[1])
    def test_02(self):
        test_login_page(self.driver,self.user[0],self.user[1])
        data = function.get_csv_line(self.data_path,1)
        test_add_page(self.driver,data[0])
        png = "test_" + time.strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,png)
        self.assertIn(AddPage(self.driver).get_alert(),data[1])
    def test_03(self):
        test_login_page(self.driver,self.user[0],self.user[1])
        data = function.get_csv_line(self.data_path,2)
        test_add_page(self.driver,data[0])
        png = "test_" + time.strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,png)
        self.assertIn(AddPage(self.driver).get_alert(),data[1])
    def test_04(self):
        test_login_page(self.driver,self.user[0],self.user[1])
        data = function.get_csv_line(self.data_path,3)
        test_add_page(self.driver,data[0])
        png = "test_" + time.strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,png)
        self.assertIn(AddPage(self.driver).get_alert(),data[1])
    def test_05(self):
        test_login_page(self.driver,self.user[0],self.user[1])
        data = function.get_csv_line(self.data_path,4)
        test_add_page(self.driver,data[0])
        png = "test_" + time.strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,png)
        self.assertIn(AddPage(self.driver).get_alert(),data[1])
    def test_06(self):
        test_login_page(self.driver,self.user[0],self.user[1])
        data = function.get_csv_line(self.data_path,5)
        test_add_page(self.driver,data[0])
        png = "test_" + time.strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,png)
        self.assertIn(AddPage(self.driver).get_alert(),data[1])
