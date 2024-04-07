import unittest
import time
from M4M.ERP_PO.HTMLTestRunner import HTMLTestRunner

test_case = "./test_case/"
discover = unittest.defaultTestLoader.discover(test_case,pattern="test_add.py")
test_report = "./test_report"
test_path = test_report + "/" + time.strftime("%H_%M_%S") + ".html"
with open(test_path,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="Test Report",description="erp test")
    runner.run(discover)
    f.close()
