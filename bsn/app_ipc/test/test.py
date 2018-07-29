#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import unittest

# import  HTMLTestRunner

if __name__ == '__main__':
    # 1、设置待执行用例的目录
    print(os.getcwd())
    test_dir = os.path.join(os.getcwd())
    print(test_dir)
    # 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    discover = unittest.defaultTestLoader.discover(
        test_dir, pattern='test_*.py')

    # 实例化TextTestRunner类
    runner = unittest.TextTestRunner()
    # runner=HTMLTestRunner.HTMLTestRunner(
    #         stream=file('testReport.html','wb'),
    #         title=u'TestReport',
    #         description=u'测试报告详细信息'
    #     )

    # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)
