#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.common import ip
from bsn.common import port
from bsn.common import ip_port


class Test(unittest.TestCase):

    def setUp(self): 
        pass

    def tearDown(self):  
        pass

    def test_2_(self):
        oIP = ip.CIP("0.0.0.0")
        oPort = port.CPort(2777)

        with self.assertRaises(ip_port.CIPPortErrParamMustIPPort):
            ip_port.CIPPort("192.0.0.1", 3333)
        with self.assertRaises(ip_port.CIPPortErrParamNotIP):
            ip_port.CIPPort(None, oPort)
        with self.assertRaises(ip_port.CIPPortErrParamNotPort):
            ip_port.CIPPort(oIP, None)

        oIPPort = ip_port.CIPPort(oIP, oPort)

        self.assertEqual(str(oIPPort), 'CIPPort("0.0.0.0",2777)')
        self.assertEqual(oIPPort.string, '0.0.0.0:2777')
        self.assertEqual(oIPPort.ip, oIP)
        self.assertEqual(oIPPort.port, oPort)


if __name__ == '__main__':
    unittest.main()
