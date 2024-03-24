import unittest
import time

from M4.ERP_PO.HTMLTestRunner import HTMLTestRunner

dc = unittest.defaultTestLoader.discover("./test_case", pattern="test_add.py")
report_path = "./test_report/" + str(time.time()) + "_result.html"
with open(report_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, description='erp test', title="Test Report")
    runner.run(dc)
    f.close()
