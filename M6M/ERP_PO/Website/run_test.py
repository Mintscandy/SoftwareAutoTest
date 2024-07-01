import time
import unittest
from M6M.ERP_PO.HTMLTestRunner import HTMLTestRunner
test_case = "./test_case"
test_report = "./test_report"

report = test_report + "/" + time.strftime("%H_%M_%S") + ".html"
discover = unittest.defaultTestLoader.discover(test_case,pattern="test_add.py")
with open(report,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="Test Report",description="erp test")
    runner.run(discover)
    f.close()

