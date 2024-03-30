import unittest
from M1.EPR_PO.Website.test_case.model import function, myunit
from M1.EPR_PO.Website.test_case.page_object.LoginPage import *
from M1.EPR_PO.Website.test_case.page_object.AddPage import *
from time import sleep
import ddt


@ddt.ddt()
class LoginTest(myunit.StartEnd):
    userinfo = ['XTGLY', '123456']
    test_data_csv = '/Users/zhudichuan/PycharmProjects/2024ERP_TR/M1/EPR_PO/Website/test_data/test_csv.csv.csv'

    def test01_add(self):
        """商品品牌名称正确新增"""
        data = function.get_csv_file(self.test_data_csv, 2)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(10)
        test_brand_add(self.driver, data[0])
        function.inser_img(self.driver, 'test01.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end!")

    def test02_add(self):
        """商品品牌名称错误新增（非汉字、英文字符类型）"""
        data = function.get_csv_file(self.test_data_csv, 3)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(4)
        test_brand_add(self.driver, data[0])
        function.inser_img(self.driver, 'test02.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end!")

    def test03_add(self):
        """商品品牌名称为空"""
        data = function.get_csv_file(self.test_data_csv, 4)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(4)
        test_brand_add(self.driver, data[0])
        function.inser_img(self.driver, 'test03.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end!")

    def test04_add(self):
        """商品品牌名称重复"""
        data = function.get_csv_file(self.test_data_csv, 5)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(4)
        test_brand_add(self.driver, data[0])
        function.inser_img(self.driver, 'test04.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end!")

    def test05_add(self):
        """字符长度小于2"""
        data = function.get_csv_file(self.test_data_csv, 6)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(4)
        test_brand_add(self.driver, data[0])
        function.inser_img(self.driver, 'test05.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end!")

    def test06_add(self):
        """字符长度小于2"""
        data = function.get_csv_file(self.test_data_csv, 7)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(4)
        test_brand_add(self.driver, data[0])
        function.inser_img(self.driver, 'test06.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end!")
