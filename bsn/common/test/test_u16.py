#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import u16
from bsn.common import err


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(err.ErrParamType):
            u16.u16(None)
        with self.assertRaises(err.ErrParamType):
            u16.u16('None')
        with self.assertRaises(err.ErrParamTooMin):
            u16.u16(-1)
        with self.assertRaises(err.ErrParamTooMax):
            u16.u16(1<<16)

        v1 = u16.u16(0)
        v2 = u16.u16('0')
        v3 = u16.u16(v1)
        self.assertEqual(str(v1), '0')
        self.assertEqual(v1, v2)
        self.assertEqual(v3, v1)
        self.assertEqual(v1.value, 0)
        self.assertEqual(v1, 0)

        v4 = u16.u16(1)
        self.assertLess(v1, v4)
        self.assertGreater(v4, v1)
        self.assertLessEqual(v1, 0)
        self.assertLessEqual(v1, 1)
        self.assertGreaterEqual(v4, 0)
        self.assertGreaterEqual(v4, 1)


if __name__ == '__main__':
    unittest.main()
