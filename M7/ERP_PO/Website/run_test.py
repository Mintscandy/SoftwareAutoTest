import unittest
import time
from M7.ERP_PO.HTMLTestRunner import HTMLTestRunner

test_dir = "./test_case"
report_dir = "./test_report"

dc = unittest.defaultTestLoader.discover(test_dir, "test_add.py")
now = time.strftime("%Y_%m_%d_%H_%M_%S")
path = report_dir + "/" + now + ".html"
with open(path, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(dc)
    f.close()
