#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import ip_port


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        with self.assertRaises(ip_port.CIPPortErr):
            ip_port.CPort(0)
        with self.assertRaises(ip_port.CIPPortErr):
            ip_port.CPort(65536)
        with self.assertRaises(ip_port.CIPPortErr):
            ip_port.CPort("2344")

        oPort = ip_port.CPort(1)
        self.assertEqual(oPort.value, 1)
        with self.assertRaises(AttributeError):
            oPort.value = 2



if __name__ == '__main__':
    unittest.main()
