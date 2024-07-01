import time
import unittest
from M10.ERP_PO.HTMLTestRunner import HTMLTestRunner

dc = unittest.defaultTestLoader.discover("./test_case", pattern="test_add.py")
report = "./test_report"
path = report + time.strftime("%H_%M_%S") + ".html"
with open(path, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(dc)
    f.close()
