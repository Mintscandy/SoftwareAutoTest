import time

from M9.ERP_PO.HTMLTestRunner import HTMLTestRunner
import unittest

dc = unittest.defaultTestLoader.discover("./test_case","test_add.py")
report = "./test_report" + str(time.strftime("%H_%M_%S")) + ".htm"
with open(report,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="Test Report",description='erp test')
    runner.run(dc)
    f.close()
