import unittest
from MZ2023.EPR_PO.HTMLTestRunner import HTMLTestRunner
from time import strftime, time

report_path = "./test_report/Test_Report"
test_case_path = "./test_case"
dc = unittest.defaultTestLoader.discover(test_case_path, pattern="test_add.py")
report = report_path + str(strftime("%H_%M_%S")) + ".html"
with open(report, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(dc)
    f.close()
