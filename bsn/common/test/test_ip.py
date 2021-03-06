#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import ip
from bsn.common import err


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(err.ErrIP):
            ip.CIP("")
        with self.assertRaises(err.ErrIP):
            ip.CIP("256.0.0.0")
        with self.assertRaises(err.ErrIP):
            ip.CIP("-1.0.0.0")
        with self.assertRaises(err.ErrIP):
            ip.CIP("1.0.0")
        with self.assertRaises(err.ErrIP):
            ip.CIP("1.0.0.0.9")

        oIP = ip.CIP("1.2.3.4")
        self.assertEqual(oIP[0], 1)
        self.assertEqual(oIP[1], 2)
        self.assertEqual(oIP[2], 3)
        self.assertEqual(oIP[3], 4)

        oIP = ip.CIP("0.0.0.0")
        self.assertEqual(oIP.u32, 0)
        self.assertEqual(str(oIP), '0.0.0.0')
        oIP = ip.CIP("0.0.0.1")
        self.assertEqual(oIP.u32, 1)
        self.assertEqual(str(oIP), '0.0.0.1')
        oIP2 = ip.CIP("0.0.0.1")
        self.assertEqual(oIP, oIP2)

        v1 = ip.CIP(oIP2)
        self.assertEqual(v1, oIP2)
        v2 = ip.CIP(v1.u32)
        self.assertEqual(v1, v2)



if __name__ == '__main__':
    unittest.main()
