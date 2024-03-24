from M5.ERP_PO.HTMLTestRunner import HTMLTestRunner
import unittest
import time

report_dir = './test_report'
test_dir = './test_case'
print("start run test case")
dc = unittest.defaultTestLoader.discover(test_dir, pattern="test_add.py")

now = time.time()
report_name = report_dir + '/' + str(now) + "_result.html"
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description='erp test')
    runner.run(dc)
    f.close()