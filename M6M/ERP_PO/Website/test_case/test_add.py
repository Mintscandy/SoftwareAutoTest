import unittest
import ddt
from time import strftime
from M6M.ERP_PO.Website.test_case.page_object.AddPage import *
from M6M.ERP_PO.Website.test_case.page_object.LogingPage import *
from M6M.ERP_PO.Website.test_case.model import myunit,function
@ddt.ddt
class final(myunit.StartEnd):
    data_path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M6M\ERP_PO\Website\test_data\test_csv.csv"
    def test_01(self):
        data = function.get_csv_line(self.data_path,0)
        test_login_page(self.driver,data[0],data[1])
        test_add_page(self.driver,data[2])
        img = "test_" + strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,img)
        po = AddPage(self.driver)
        self.assertIn(data[3],po.get_alert())
    def test_02(self):
        data = function.get_csv_line(self.data_path,1)
        test_login_page(self.driver,data[0],data[1])
        test_add_page(self.driver,data[2])
        img = "test_" + strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,img)
        po = AddPage(self.driver)
        self.assertIn(data[3],po.get_alert())
    def test_03(self):
        data = function.get_csv_line(self.data_path,2)
        test_login_page(self.driver,data[0],data[1])
        test_add_page(self.driver,data[2])
        img = "test_" + strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,img)
        po = AddPage(self.driver)
        self.assertIn(data[3],po.get_alert())
    def test_04(self):
        data = function.get_csv_line(self.data_path,3)
        test_login_page(self.driver,data[0],data[1])
        test_add_page(self.driver,data[2])
        img = "test_" + strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,img)
        po = AddPage(self.driver)
        self.assertIn(data[3],po.get_alert())
    def test_05(self):
        data = function.get_csv_line(self.data_path,4)
        test_login_page(self.driver,data[0],data[1])
        test_add_page(self.driver,data[2])
        img = "test_" + strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,img)
        po = AddPage(self.driver)
        self.assertIn(data[3],po.get_alert())
    def test_06(self):
        data = function.get_csv_line(self.data_path,5)
        test_login_page(self.driver,data[0],data[1])
        test_add_page(self.driver,data[2])
        img = "test_" + strftime("%H_%M_%S") + ".png"
        function.inser_img(self.driver,img)
        po = AddPage(self.driver)
        self.assertIn(data[3],po.get_alert())


