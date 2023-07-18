import unittest
# from MyTestCase1 import TestMyCase1
# from MyTestCase2 import TestMyCase2
# import MyTestCase3_Module
import os

from unitest.util.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    report_dir = "./reports/"
    report_file = report_dir + "html_report.html"

    # 判断reports目录是否存在，如果不存在就创建目录
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    with open(report_file, "wb") as fl:
        module_path = "./"
        discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="test*.py")
        runner = HTMLTestRunner(title='Test标题', description='描述本次测试的大概内容', stream=fl)
        runner.run(discover)
