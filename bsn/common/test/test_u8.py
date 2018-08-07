#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import u8
from bsn.common import err


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(err.ErrParamType):
            u8.u8(None)
        with self.assertRaises(err.ErrParamType):
            u8.u8('None')
        with self.assertRaises(err.ErrParamTooMin):
            u8.u8(-1)
        with self.assertRaises(err.ErrParamTooMax):
            u8.u8(1<<8)

        v1 = u8.u8(0)
        v2 = u8.u8('0')
        v3 = u8.u8(v1)
        self.assertEqual(str(v1), '0')
        self.assertEqual(v1, v2)
        self.assertEqual(v3, v1)
        self.assertEqual(v1.value, 0)
        self.assertEqual(v1, 0)
        self.assertEqual(0, v1)

        v4 = u8.u8(1)
        self.assertLess(v1, v4)
        self.assertGreater(v4, v1)
        self.assertLessEqual(v1, 0)
        self.assertLessEqual(v1, 1)
        self.assertGreaterEqual(v4, 0)
        self.assertGreaterEqual(v4, 1)


if __name__ == '__main__':
    unittest.main()
