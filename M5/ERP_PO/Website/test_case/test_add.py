from M5.ERP_PO.Website.test_case.page_object.BasePage import *
from M5.ERP_PO.Website.test_case.page_object.LoginPage import *
from M5.ERP_PO.Website.test_case.page_object.AddPage import *
from M5.ERP_PO.Website.test_case.model import function, myunit
from M5.ERP_PO.driver.driver import *
from time import sleep


class final(myunit.StartEnd):
    user_info = ["XTGLY", "123456"]
    csv = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M5\ERP_PO\Website\test_data\test_csv.csv"

    def test01(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(1)
        data = function.get_csv_line(self.csv, 0)
        test_add_page(self.driver, data[0])
        sleep(2)
        function.inser_png(self.driver, "t1.png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test02(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(1)
        data = function.get_csv_line(self.csv, 1)
        test_add_page(self.driver, data[0])
        sleep(2)
        function.inser_png(self.driver, "t2.png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test03(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(1)
        data = function.get_csv_line(self.csv, 2)
        test_add_page(self.driver, data[0])
        sleep(2)
        function.inser_png(self.driver, "t3.png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test04(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(1)
        data = function.get_csv_line(self.csv, 3)
        test_add_page(self.driver, data[0])
        sleep(2)
        function.inser_png(self.driver, "t4.png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test05(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(1)
        data = function.get_csv_line(self.csv, 4)
        test_add_page(self.driver, data[0])
        sleep(2)
        function.inser_png(self.driver, "t5.png")
        self.assertIn(Add(self.driver).get_alert(), data[1])

    def test06(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(1)
        data = function.get_csv_line(self.csv, 5)
        test_add_page(self.driver, data[0])
        sleep(2)
        function.inser_png(self.driver, "t6.png")
        self.assertIn(Add(self.driver).get_alert(), data[1])


