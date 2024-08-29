import time

from M8.ERP_PO.HTMLTestRunner import HTMLTestRunner
import unittest
discover = unittest.defaultTestLoader.discover(start_dir="./test_case", pattern="test_add.py")
# time：“%Y-%m-%d %H-%M-%S”
# 这里是因为我懒 啊哈哈哈哈 懂滴  我时长忘记加% 我经常记不住大小写 哈哈哈 我给你写好了 你应该记得住了 嘿嘿我可以看文档
now = "./test_report/" + time.strftime("%H_%M_%S") + ".html"
with open(now, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(discover)
    # f.close用不到呀，因为你在myunit.py里面写了self.driver.quit()
    # 嘿嘿 这里欣欣讲错咯 是因为这是with open 所有不用f.close
    # 好好好，故意给我挖陷阱
    f.close()