import unittest
from M2.ERP_PO.Website.test_case.model import function, myunit
from M2.ERP_PO.Website.test_case.page_object.LoginPage import *
from M2.ERP_PO.Website.test_case.page_object.AddPage import *
from time import sleep
import ddt


class AddTest(myunit.StartEnd):
    userinfo = ["XTGLY", '123456']
    test_data_csv = '/Users/zhudichuan/PycharmProjects/2024ERP_TR/M2/ERP_PO/Website/test_data/test_csv.csv'

    def test01_add(self):
        """商品分类名称正确新增"""
        data = function.get_csv_file(self.test_data_csv, 1)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(2)
        test_category_add(self.driver, data[0])
        function.inser_img(self.driver, 'test01.png')
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end！")

    def test02_add(self):
        """商品分类名称错误新增（为空）"""
        data = function.get_csv_file(self.test_data_csv, 2)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(2)
        test_category_add(self.driver, data[0])
        function.inser_img(self.driver, 'test02.png')
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end！")

    def test03_add(self):
        """商品分类名称错误新增（重复）"""
        data = function.get_csv_file(self.test_data_csv, 3)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(2)
        test_category_add(self.driver, data[0])
        function.inser_img(self.driver, 'test03.png')
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end！")

    def test04_add(self):
        """商品分类名称错误新增（非汉字、英文字符类型）"""
        data = function.get_csv_file(self.test_data_csv, 4)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(2)
        test_category_add(self.driver, data[0])
        function.inser_img(self.driver, 'test04.png')
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end！")

    def test05_add(self):
        """商品分类名称错误新增（字符长度小于2）"""
        data = function.get_csv_file(self.test_data_csv, 5)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(2)
        test_category_add(self.driver, data[0])
        function.inser_img(self.driver, 'test05.png')
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end！")

    def test06_add(self):
        """商品分类名称错误新增（字符长度大于20）"""
        data = function.get_csv_file(self.test_data_csv, 6)
        test_user_login(self.driver, self.userinfo[0], self.userinfo[1])
        sleep(2)
        test_category_add(self.driver, data[0])
        function.inser_img(self.driver, 'test06.png')
        po = AddPage(self.driver)
        print(po.get_alert())
        self.assertIn(data[1], po.get_alert())
        print("test case is successful test end！")
