#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.template import add
from bsn.template import dec
from bsn.common import msg



class LuaTest(unittest.TestCase):

    def setUp(self): 
        self._CMsg = msg.CMsg()

    def tearDown(self):  
        pass
        
    def test_2_add(self):
        self.assertEqual(str(self._CMsg), 'head=[cmd=0 length=0] body=[None]')
        self._CMsg.cmd = 1
        self.assertEqual(str(self._CMsg), 'head=[cmd=1 length=0] body=[None]')
        self._CMsg.body = b''
        self.assertEqual(str(self._CMsg), "head=[cmd=1 length=0] body=[b'']")
        self._CMsg.body = b'a'
        self.assertEqual(str(self._CMsg), "head=[cmd=1 length=1] body=[b'a']")
        self._CMsg.body = b'abc'
        self.assertEqual(str(self._CMsg), "head=[cmd=1 length=3] body=[b'abc']")
        byData = self._CMsg.serialize()
        self.assertEqual(len(byData), 7)
        oCMsg = msg.CMsg()
        uLength = oCMsg.parse(byData)
        self.assertEqual(uLength, 7)
        self.assertEqual(str(oCMsg), "head=[cmd=1 length=3] body=[b'abc']")

      

if __name__ == '__main__':
    unittest.main()
