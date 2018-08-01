#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import u16


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(u16.ErrParamType):
            u16.u16(None)
        with self.assertRaises(u16.ErrParamType):
            u16.u16('None')
        with self.assertRaises(u16.ErrParamTooMin):
            u16.u16(-1)
        with self.assertRaises(u16.ErrParamTooMax):
            u16.u16(1<<16)

        v1 = u16.u16(0)
        v2 = u16.u16('0')
        v3 = u16.u16(v1)
        self.assertEqual(str(v1), '0')
        self.assertEqual(v1, v2)
        self.assertEqual(v3, v1)





if __name__ == '__main__':
    unittest.main()
