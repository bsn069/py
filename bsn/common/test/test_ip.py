#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import ip_ip


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(ip_ip.CIPErr):
            ip_ip.CIP(0)
        with self.assertRaises(ip_ip.CIPErr):
            ip_ip.CIP("")
        with self.assertRaises(ip_ip.CIPErr):
            ip_ip.CIP("256.0.0.0")
        with self.assertRaises(ip_ip.CIPErr):
            ip_ip.CIP("-1.0.0.0")
        with self.assertRaises(ip_ip.CIPErr):
            ip_ip.CIP("1.0.0")
        with self.assertRaises(ip_ip.CIPErr):
            ip_ip.CIP("1.0.0.0.9")

        oIP = ip_ip.CIP("0.0.0.0")
        self.assertEqual(oIP.u32, 0)
        oIP = ip_ip.CIP("0.0.0.1")
        self.assertEqual(oIP.u32, 1)



if __name__ == '__main__':
    unittest.main()
