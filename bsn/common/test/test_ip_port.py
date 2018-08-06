#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import ip
from bsn.common import port
from bsn.common import ip_port
from bsn.common import err


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        oIP = ip.CIP("0.0.0.0")
        oPort = port.CPort(2777)

        with self.assertRaises(err.ErrParamNotIP):
            ip_port.CIPPort(None, oPort)
        with self.assertRaises(err.ErrParamNotPort):
            ip_port.CIPPort(oIP, None)

        v1 = ip_port.CIPPort(oIP, oPort)
        self.assertEqual(str(v1), 'CIPPort("0.0.0.0",2777)')
        self.assertEqual(v1.string, '0.0.0.0:2777')
        self.assertEqual(v1.ip, oIP)
        self.assertEqual(v1.port, oPort)

        v2 = ip_port.CIPPort("0.0.0.0", 2777)
        self.assertEqual(v1, v2)

        v3 = ip_port.CIPPort("0.0.0.0", "2777")
        self.assertEqual(v1, v3)


if __name__ == '__main__':
    unittest.main()
