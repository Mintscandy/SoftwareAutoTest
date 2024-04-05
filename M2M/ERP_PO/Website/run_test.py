import time
from M2M.ERP_PO.HTMLTestRunner import HTMLTestRunner
import unittest

case_dir = "./test_case"
report_dir = "./test_report/"

discover = unittest.defaultTestLoader.discover(case_dir, "test_add.py")
report = report_dir + "test_report" + str(time.strftime("%H_%M_%S")) + ".htm"
with open(report, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(discover)
    f.close()
