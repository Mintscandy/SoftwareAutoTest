import unittest
import ddt
from M8_1.ERP_PO.Website.test_case.model.function import *
from M8_1.ERP_PO.Website.test_case.model.myunit import *
from M8_1.ERP_PO.Website.test_case.page_object.AddPage import *
from M8_1.ERP_PO.Website.test_case.page_object.LoginPage import *


@ddt.ddt()
class test_final(StartEnd):
    data_file = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M8_1\ERP_PO\Website\test_data\test_csv.csv'

    def test_01(self):
        data = read_csv_line(self.data_file, 0)
        test_login_page(self.driver, data[0], data[1])
        # 这个地方你不用等待2s，就像我那个地方说的，这个地方属于智能等待时间
        sleep(2)
        test_add_page(self.driver, data[2])
        # 这个地方也不用哦，因为我们在AddFunction里面最后面加2s等待
        sleep(1)
        page = AddPage(self.driver)
        inser_img(self.driver, "screen_test_01.png")
        self.assertIn(data[3], page.get_alert())

    def test_02(self):
        data = read_csv_line(self.data_file, 1)
        test_login_page(self.driver, data[0], data[1])
        sleep(2)
        test_add_page(self.driver, data[2])
        sleep(1)
        page = AddPage(self.driver)
        inser_img(self.driver, "screen_test_02.png")
        self.assertIn(data[3], page.get_alert())

    def test_03(self):
        data = read_csv_line(self.data_file, 2)
        test_login_page(self.driver, data[0], data[1])
        sleep(2)
        test_add_page(self.driver, data[2])
        sleep(1)
        page = AddPage(self.driver)
        inser_img(self.driver, "screen_test_03.png")
        self.assertIn(data[3], page.get_alert())

    def test_04(self):
        data = read_csv_line(self.data_file, 3)
        test_login_page(self.driver, data[0], data[1])
        sleep(2)
        test_add_page(self.driver, data[2])
        sleep(1)
        page = AddPage(self.driver)
        inser_img(self.driver, "screen_test_04.png")
        self.assertIn(data[3], page.get_alert())

    def test_05(self):
        data = read_csv_line(self.data_file, 4)
        test_login_page(self.driver, data[0], data[1])
        sleep(2)
        test_add_page(self.driver, data[2])
        sleep(1)
        page = AddPage(self.driver)
        inser_img(self.driver, "screen_test_05.png")
        self.assertIn(data[3], page.get_alert())
