#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.template import add
from bsn.template import dec
from bsn.common import msg_head


class LuaTest(unittest.TestCase):

    def setUp(self): 
        self._CMsgHead = msg_head.CMsgHead()

    def tearDown(self):  
        print(__name__ + ' tearDown\n')
        
    def test_2_add(self):
        self._CMsgHead.cmd = 1
        self._CMsgHead.length = 2
        byData = self._CMsgHead.serialize()
        self.assertEqual(len(byData), self._CMsgHead.Bit)
        self._CMsgHeadOut = msg_head.CMsgHead()
        self._CMsgHeadOut.parse(byData)
        self.assertEqual(self._CMsgHeadOut.cmd,1)
        self.assertEqual(self._CMsgHeadOut.length,2)
        print(self._CMsgHeadOut)

        self._CMsgHead.cmd = 65535
        self._CMsgHead.length = 65535
        byData = self._CMsgHead.serialize()
        self.assertEqual(len(byData), self._CMsgHead.Bit)
        self._CMsgHeadOut = msg_head.CMsgHead()
        self._CMsgHeadOut.parse(byData)
        self.assertEqual(self._CMsgHeadOut.cmd,65535)
        self.assertEqual(self._CMsgHeadOut.length,65535)

      

if __name__ == '__main__':
    unittest.main()
