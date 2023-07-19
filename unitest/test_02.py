# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 7:02
# @Author  : DuYiB
# @FileName: test_xzys.py
# @Software: PyCharm
import os

from ddt import data, ddt, unpack

from unitest.util.HTMLTestRunner import HTMLTestRunner
import requests
import time
import unittest


@ddt
class TestXzys(unittest.TestCase):

    @data(
        {"first": 3, "second": 2},
        {"first": 4, "second": 1},
        {"first": 8, "second": 6}
    )
    @unpack
    def test_greater(self, second, first):
        print("second", second, "first", first)

    @data(
        (3, 2),
        (4, 1),
        (8, 6))
    @unpack
    def test_greater2(self, v1, v2):
        print("v1", v1, "v2", v2)

        # v1 3 v2 2
        # v1 4 v2 1
        # v1 8 v2 6

    @data(
        (3, 2),
        (4, 1),
        (8, 6))
    def test_greater3(self, v1):
        print("v1111111111", v1)
        # v1111111111(3, 2)
        # v1111111111(4, 1)
        # v1111111111(8, 6)


if __name__ == '__main__':
    unittest.main()
