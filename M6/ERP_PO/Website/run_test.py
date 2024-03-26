import time

from M6.ERP_PO.HTMLTestRunner import HTMLTestRunner
from time import sleep
import unittest

test_dir = './test_case'
report_dir = './test_report'

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_add.py")
now = time.strftime("%Y_%m_%d_%H_%M_%S")

fp = report_dir + "/" + now + "_result.html"
with open(fp, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(discover)
    f.close()
