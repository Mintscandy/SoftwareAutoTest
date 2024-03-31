from M10.ERP_PO.Website.test_case.page_object.LoginPage import *
from M10.ERP_PO.Website.test_case.page_object.BasePage import *
from M10.ERP_PO.Website.test_case.page_object.AddPage import *
import ddt

from M10.ERP_PO.Website.test_case.model import function, myunit


@ddt.ddt()
class final(myunit.StartEnd):
    user = ["XTGLY", "123456"]
    data_csv = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M10\ERP_PO\Website\test_data\test_csv.csv"

    def test01(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_csv, 0)

        test_add_page(self.driver, data[0])
        png = "test" + str(time.time()) + ".png"

        function.inser_img(self.driver, png)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test02(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_csv, 1)

        test_add_page(self.driver, data[0])
        png = "test" + str(time.time()) + ".png"

        function.inser_img(self.driver, png)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test03(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_csv, 2)

        test_add_page(self.driver, data[0])
        png = "test" + str(time.time()) + ".png"

        function.inser_img(self.driver, png)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test04(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_csv, 3)

        test_add_page(self.driver, data[0])
        png = "test" + str(time.time()) + ".png"

        function.inser_img(self.driver, png)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test05(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_csv, 4)

        test_add_page(self.driver, data[0])
        png = "test" + str(time.time()) + ".png"

        function.inser_img(self.driver, png)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])

    def test06(self):
        test_login_page(self.driver, self.user[0], self.user[1])
        data = function.get_csv_line(self.data_csv, 5)

        test_add_page(self.driver, data[0])
        png = "test" + str(time.time()) + ".png"

        function.inser_img(self.driver, png)
        self.assertIn(AddPage(self.driver).get_alert(), data[1])


