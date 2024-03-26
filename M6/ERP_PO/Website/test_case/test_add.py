import time
from time import sleep
from M6.ERP_PO.Website.test_case.page_object.LoginPage import *
from M6.ERP_PO.Website.test_case.page_object.AddPage import *
from M6.ERP_PO.Website.test_case.page_object.BasePage import *
from M6.ERP_PO.Website.test_case.model import function, myunit
import ddt
import unittest


@ddt.ddt()
class final(myunit.StartEnd):
    path = r'C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M6\ERP_PO\Website\test_data\test_csv.csv'
    case_data = function.read_csv(path)

    user = ["XTGLY", "123456"]

    @ddt.data(*case_data)
    def test01(self, l):
        print("test case start")
        test_login_page(self.driver, self.user[0], self.user[1])
        sleep(3)
        test_add_page(self.driver, l[0])
        function.inser_img(self.driver, "test_" + time.strftime("%Y:%m:d_%H:%M:%S") + ".png")

        self.assertIn(Add(self.driver).get_alert(), l[1])


if __name__ == '__main__':
    unittest.main()
