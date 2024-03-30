from M7.ERP_PO.Website.test_case.page_object.AddPage import *
from M7.ERP_PO.Website.test_case.page_object.LoginPage import *
from M7.ERP_PO.Website.test_case.page_object.BasePage import *
from time import sleep
import ddt
from M7.ERP_PO.Website.test_case.model import function, myunit


@ddt.ddt()
class Test(myunit.StartEnd):
    user_info = ["XTGLY", "123456"]
    path = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M7\ERP_PO\Website\test_data\test_csv.csv"

    def test01(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(2)
        data = function.read_csv_line(self.path)
        test_add_page(self.driver, data[0][0])
        function.inser_img(self.driver, "test01.png")
        self.assertIn(AddPage(self.driver).get_alert(), data[0][1])

    def test02(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(2)
        data = function.read_csv_line(self.path)
        test_add_page(self.driver, data[1][0])
        function.inser_img(self.driver, "test02.png")
        self.assertIn(AddPage(self.driver).get_alert(), data[1][1])

    def test03(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(2)
        data = function.read_csv_line(self.path)
        test_add_page(self.driver, data[2][0])
        function.inser_img(self.driver, "test02.png")
        self.assertIn(AddPage(self.driver).get_alert(), data[2][1])

    def test04(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(2)
        data = function.read_csv_line(self.path)
        test_add_page(self.driver, data[3][0])
        function.inser_img(self.driver, "test01.png")
        self.assertIn(AddPage(self.driver).get_alert(), data[3][1])

    def test05(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(2)
        data = function.read_csv_line(self.path)
        test_add_page(self.driver, data[4][0])
        function.inser_img(self.driver, "test01.png")
        self.assertIn(AddPage(self.driver).get_alert(), data[4][1])

    def test06(self):
        test_login_page(self.driver, self.user_info[0], self.user_info[1])
        sleep(2)
        data = function.read_csv_line(self.path)
        test_add_page(self.driver, data[5][0])
        function.inser_img(self.driver, "test01.png")
        self.assertIn(AddPage(self.driver).get_alert(), data[5][1])