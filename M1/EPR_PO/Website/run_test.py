import unittest
from M1.EPR_PO.Website.test_case.model.function import *
from M1.EPR_PO.HTMLTestRunner import HTMLTestRunner
import time

report_dir = './test_report'
test_dir = './test_case'
print('start run test case')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_add.py')

now = time.strftime("%Y-%m-%d %H:%MZ2023:%S")
report_name = report_dir + '/' + now + '_result.html'

with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='Test Report', description='erp test')
    runner.run(discover)
    f.close()
