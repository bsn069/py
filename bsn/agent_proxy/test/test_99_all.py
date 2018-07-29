#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from bsn.agent_proxy.agent_proxy import CAgentProxy


class Test(unittest.TestCase):

    def setUp(self): 
        self.__agent_proxy = CAgentProxy()
        pass

    def tearDown(self):  
        pass
        
    def test_2_(self):
        self.assertEqual(self.__agent_proxy.port, None)
        with self.assertRaises(TypeError):
            self.__agent_proxy.port = 0
        self.assertEqual(self.__agent_proxy.port, None)
        with self.assertRaises(TypeError):
            self.__agent_proxy.port = 65536
        self.assertEqual(self.__agent_proxy.port, None)
        with self.assertRaises(TypeError):
            self.__agent_proxy.port = '10000'
        self.assertEqual(self.__agent_proxy.port, None)
    
        self.__agent_proxy.port = 1000
        self.assertEqual(self.__agent_proxy.port, 1000)
        with self.assertRaises(TypeError):
            self.__agent_proxy.port = 2000
        self.assertEqual(self.__agent_proxy.port, 1000)

if __name__ == '__main__':
    unittest.main()
