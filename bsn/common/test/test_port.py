#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import port
from bsn.common import err


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(err.ErrPort):
            port.CPort(None)
        with self.assertRaises(err.ErrPort):
            port.CPort(0)
        with self.assertRaises(err.ErrPort):
            port.CPort(65536)

        v1 = port.CPort(1)
        v2 = port.CPort('1')
        v3 = port.CPort(v1)

        self.assertEqual(str(v1), '1')
        self.assertEqual(v1.value, 1)
        self.assertEqual(v1, v2)
        self.assertEqual(v1, v3)
        self.assertEqual(v1, 1)


if __name__ == '__main__':
    unittest.main()
