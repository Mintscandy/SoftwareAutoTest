from M5.ERP_PO.HTMLTestRunner import HTMLTestRunner
import unittest
import time

dc = unittest.defaultTestLoader.discover("./test_case", pattern="test_add.py")
now = str(time.time())

report_dir = r"C:\Users\Mints_Candy\Desktop\SoftwareAutoTest\M5\ERP_PO\Website\test_report\\"
with open(report_dir+"test_" + now + "_.html", "wb") as f:
    runner = HTMLTestRunner(stream=f, description='erp test', title="Test Report")
    runner.run(dc)
    f.close()
