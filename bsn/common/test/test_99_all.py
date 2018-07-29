#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.template import add
from bsn.template import dec


class LuaTest(unittest.TestCase):

    def setUp(self): 
        print(__name__ + ' setUp\n')

    def tearDown(self):  
        print(__name__ + ' tearDown\n')
        
    def test_2_add(self):
        print(add)
        print(add.add)
        print(add.add(1,1))

    def test_1_dec(self):
        print(dec)
        print(dec.dec)
        print(dec.dec(1,1))

if __name__ == '__main__':
    unittest.main()
