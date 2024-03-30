import time
import unittest
import ddt
from M3.ERP_PO.Website.test_case.page_object.BasePage import *
from M3.ERP_PO.Website.test_case.page_object.LoginPage import *
from M3.ERP_PO.Website.test_case.page_object.AddPage import *
from M3.ERP_PO.Website.test_case.model import myunit, function


class final_ts(myunit.StartEnd):
    user_info = ['XTGLY', '123456']
    data_csv = '/Users/zhudichuan/PycharmProjects/2024ERP_TR/M3/ERP_PO/Website/test_data/test_csv.csv.csv'

    def test01(self):
        """商品分类名称正确新增"""
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_data(self.data_csv, 0)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, 'test01.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(po.get_alert(), data[1])

    def test02(self):
        """商品分类名称错误新增(为空）"""
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_data(self.data_csv, 1)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, 'test02.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(po.get_alert(), data[1])

    def test03(self):
        """商品分类名称错误新增(重复）"""
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_data(self.data_csv, 2)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, 'test03.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(po.get_alert(), data[1])

    def test04(self):
        """商品分类名称错误新增(非汉字、英文字符类型）"""
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_data(self.data_csv, 3)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, 'test04.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(po.get_alert(), data[1])

    def test05(self):
        """商品分类名称错误新增(字符长度小于2）"""
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_data(self.data_csv, 4)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, 'test05.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(po.get_alert(), data[1])

    def test06(self):
        """商品分类名称错误新增(字符长度大于20）"""
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        data = function.get_csv_data(self.data_csv, 5)

        test_add_page(self.driver, data[0])
        function.inser_img(self.driver, 'test06.png')
        po = Add(self.driver)
        print(po.get_alert())
        self.assertIn(po.get_alert(), data[1])

