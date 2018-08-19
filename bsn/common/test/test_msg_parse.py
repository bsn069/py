#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.template import add
from bsn.template import dec
from bsn.common import msg_parse

class CMsgParse(msg_parse.CMsgParse):
    def __init__(self):
        super().__init__()
        self._CMsgs = []

    def on_recv_msg(self, oCMsg):
        self._CMsgs.append(oCMsg)

class LuaTest(unittest.TestCase):

    def setUp(self): 
        self._CMsgParse = CMsgParse()

    def tearDown(self):  
        print(__name__ + ' tearDown\n')
        
    def test_2_add(self):
       

      

if __name__ == '__main__':
    unittest.main()
