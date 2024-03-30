import time

from M8.ERP_PO.HTMLTestRunner import HTMLTestRunner
import unittest

dc = unittest.defaultTestLoader.discover(start_dir="./test_case", pattern="test_add.py")
now = "./test_report/" + time.strftime("%H_%M_%S") + ".html"
with open(now, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(dc)
    f.close()
