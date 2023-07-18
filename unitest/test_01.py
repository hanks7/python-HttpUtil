# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 7:02
# @Author  : DuYiB
# @FileName: test_xzys.py
# @Software: PyCharm
import os

from unitest.util.HTMLTestRunner import HTMLTestRunner
import requests
import time
import unittest


class TestXzys(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        print("结束")

    url = "http://web.juhe.cn:8080/constellation/getAll"

    def test_top(self):
        data = "key=ce06d65173eaaf9a96559db02f9fec18&consName=金牛座&type=today"
        res = requests.get(url=self.url, params=data)
        njson = res.json()
        self.assertEqual(res.status_code, 200, msg='状态码为200')
        self.assertEqual(njson['error_code'], 0, msg="错误码为0")

    def test_top_key_void(self):
        data = "consName=金牛座&type=today"
        res = requests.get(url=self.url, params=data)
        njson = res.json()
        self.assertEqual(res.status_code, 200, msg='状态码为200')
        self.assertEqual(njson['error_code'], 10001, msg="错误码为0")

    def test_top_cosName_void(self):
        data = "key=ce06d65173eaaf9a96559db02f9fec18&type=today"
        res = requests.get(url=self.url, params=data)
        njson = res.json()
        self.assertEqual(res.status_code, 200, msg='状态码为200')
        self.assertEqual(njson['error_code'], 205801, msg="错误码为0")

    def test_top_type_void(self):
        data = "key=ce06d65173eaaf9a96559db02f9fec18&consName=金牛座&type=duyibo"
        res = requests.get(url=self.url, params=data)
        njson = res.json()
        self.assertEqual(res.status_code, 200, msg='状态码为200')
        self.assertEqual(njson['error_code'], 205801, msg="错误码为0")

    def test_top_key_error(self):
        data = "key=ce06d65173eaaf9a96559db02f9fadwaec18&consName=金牛座&type=today"
        res = requests.get(url=self.url, params=data)
        njson = res.json()
        self.assertEqual(res.status_code, 200, msg='状态码为200')
        self.assertEqual(njson['error_code'], 10001, msg="错误码为0")


if __name__ == '__main__':
    unittest.main()
